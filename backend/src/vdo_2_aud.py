import subprocess
import os
import shutil
from pathlib import Path
import imageio_ffmpeg as ffmpeg

SRC_DIR = Path(__file__).resolve().parent


def file_manager(user_path):
    # Ensure working directories exist (absolute paths — safe from any cwd)
    for f in ["Video", "Audio", "Transcripted_json", "Managed_chunk", "parquet_files", "saved_parquets"]:
        os.makedirs(SRC_DIR / f, exist_ok=True)

    normalized_path = os.path.normpath(user_path)

    if os.path.isfile(normalized_path):
        file_name = os.path.basename(normalized_path)
        dest_path = str(SRC_DIR / "Video" / file_name)
        if not os.path.exists(dest_path) or not os.path.samefile(normalized_path, dest_path):
            shutil.copy(normalized_path, dest_path)
    elif os.path.isdir(normalized_path):
        files = os.listdir(normalized_path)
        for file in files:
            full_path = os.path.join(normalized_path, file)
            if os.path.isfile(full_path):
                dest_path = str(SRC_DIR / "Video" / file)
                if not os.path.exists(dest_path) or not os.path.samefile(full_path, dest_path):
                    shutil.copy(full_path, dest_path)
    else:
        raise FileNotFoundError(f"Path does not exist: {user_path}")


def processor(input_file, output_file):
    exe = ffmpeg.get_ffmpeg_exe()
    subprocess.run([
        exe, "-i", str(SRC_DIR / "Video" / input_file),
        "-vn", "-acodec", "mp3", str(SRC_DIR / "Audio" / f"{output_file}.mp3")
    ], check=True)
