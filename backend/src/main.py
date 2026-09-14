import os
import shutil
import requests
from pathlib import Path
from .vdo_2_aud import file_manager, processor
from .transcription import transformer
from .config import model, output_model
from .chunking import manage_chunk
from .save_all_chunks import save_chunk
from .embeds import create_db
from .prompt import inference, prompt
from .essential_functions import delete_files_and_create_parquet, eval_func


class Main:
    def __init__(self, path, filename, test) -> None:
        self.path = path
        self.file_name = filename
        self.test = test
        self.vdo_2_aud_func = None
        self.chunking_func = None
        self.embeds_func = None
        self.prompt_func = None
        self.save_all_chunks_func = None
        self.transcription_func = None

    def main_func(self):
        os.chdir(Path(__file__).resolve().parent)
        if not self.path.endswith(".parquet"):
            try:
                file_manager(self.path)
            except Exception as e:
                print(f"[Error] vdo_2_aud.py — file_manager: {e}")

            for vdo in os.listdir("Video"):
                try:
                    if not vdo.endswith(".gitkeep"):
                        processor(vdo, self.file_name)
                    if self.test:
                        self.vdo_2_aud_func = True

                except Exception as e:
                    print(f"[Error] vdo_2_aud.py — processor: {e}")
                    if self.test:
                        self.vdo_2_aud_func = False

            for aud in os.listdir("Audio"):
                try:
                    if not aud.endswith(".gitkeep"):
                        transformer(aud, model)
                    if self.test:
                        self.transcription_func = True

                except Exception as e:
                    print(f"[Error] transcription.py: {e}")
                    if self.test:
                        self.transcription_func = False

            for jsons in os.listdir("Transcripted_json"):
                try:
                    if not jsons.endswith(".gitkeep"):
                        manage_chunk(jsons)
                    if self.test:
                        self.chunking_func = True

                except Exception as e:
                    print(f"[Error] chunking.py: {e}")
                    if self.test:
                        self.chunking_func = False

            try:
                save_chunk(os.listdir("Managed_chunk"))
                if self.test:
                    self.save_all_chunks_func = True

            except Exception as e:
                print(f"[Error] save_all_chunks.py: {e}")
                if self.test:
                    self.save_all_chunks_func = False

            try:
                create_db(self.file_name)
                if self.test:
                    self.embeds_func = True

            except Exception as e:
                print(f"[Error] embeds.py: {e}")
                if self.test:
                    self.embeds_func = False

        while True:
            if self.test:
                user_query = "What is this video about?"
            else:
                user_query = input("ask anything related to the video you shared (type quit or exit to stop the program) : ")
            if user_query.lower() == "quit" or user_query.lower() == "exit":
                delete_files_and_create_parquet(self.file_name)
                break
            else:
                try:
                    generated_prompt = prompt(self.file_name, user_query, self.test, self.path)
                    print(inference(generated_prompt, output_model))
                    print('-----------------------------------------------------------------------------------------------')
                    self.prompt_func = True

                except requests.exceptions.ConnectionError:
                    print("[Error]: Ollama is not running — please start it and try again.")
                    self.prompt_func = False

                except Exception as e:
                    print(f"[Error] prompt.py: {e}")
                    self.prompt_func = False

            if self.test:
                delete_files_and_create_parquet(self.file_name)
                break

        eval_func(self.test, self.path, self.vdo_2_aud_func, self.chunking_func, self.embeds_func, self.prompt_func, self.save_all_chunks_func, self.transcription_func)
