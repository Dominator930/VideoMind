import os
from pathlib import Path
from PySide6.QtCore import QThread, Signal

from backend.src.vdo_2_aud import file_manager, processor
from backend.src.transcription import transformer
from backend.src.config import model, output_model
from backend.src.chunking import manage_chunk
from backend.src.save_all_chunks import save_chunk
from backend.src.embeds import create_db
from backend.src.prompt import inference, prompt

# Absolute path to backend/src — used for all file operations to avoid
# os.chdir() global state mutation in worker threads.
SRC_DIR = Path(__file__).resolve().parent.parent / "backend" / "src"


class VideoProcessorWorker(QThread):
    progress = Signal(int, str)
    finished = Signal(bool, str)

    def __init__(self, file_path, file_name):
        super().__init__()
        self.file_path = file_path
        self.file_name = file_name

    def run(self):
        try:
            src = SRC_DIR

            if self.file_path.endswith(".parquet"):
                self.progress.emit(100, "Parquet vector database loaded!")
                self.finished.emit(True, self.file_name)
                return

            self.progress.emit(10, "Staging video file...")
            file_manager(self.file_path)

            self.progress.emit(25, "Extracting audio from video...")
            for vdo in os.listdir(src / "Video"):
                if not vdo.endswith(".gitkeep"):
                    # processor uses os.path.join("Video", ...) internally — run from src
                    os.chdir(src)
                    processor(vdo, self.file_name)

            self.progress.emit(50, "Transcribing speech to text with Whisper...")
            os.chdir(src)
            for aud in os.listdir(src / "Audio"):
                if not aud.endswith(".gitkeep"):
                    transformer(aud, model)

            self.progress.emit(75, "Chunking transcription segments...")
            os.chdir(src)
            for jsons in os.listdir(src / "Transcripted_json"):
                if not jsons.endswith(".gitkeep"):
                    manage_chunk(jsons)

            self.progress.emit(85, "Saving managed chunks...")
            os.chdir(src)
            save_chunk(os.listdir(src / "Managed_chunk"))

            self.progress.emit(95, "Generating embeddings via Ollama bge-m3...")
            os.chdir(src)
            create_db(self.file_name)

            self.progress.emit(100, "Video processing complete!")
            self.finished.emit(True, self.file_name)

        except Exception as e:
            print(f"[Worker Error] Processing failed: {e}")
            self.finished.emit(False, str(e))


class QueryWorker(QThread):
    result = Signal(str, str)

    def __init__(self, file_name, user_query):
        super().__init__()
        self.file_name = file_name
        self.user_query = user_query

    def run(self):
        try:
            from backend.src.config import output_model
            os.chdir(SRC_DIR)
            generated_prompt = prompt(self.file_name, self.user_query)
            ans = inference(generated_prompt, output_model)
            self.result.emit(self.user_query, ans)
        except Exception as e:
            err_msg = f"I encountered an error querying the model. Please ensure Ollama is running.\nDetails: {e}"
            self.result.emit(self.user_query, err_msg)
