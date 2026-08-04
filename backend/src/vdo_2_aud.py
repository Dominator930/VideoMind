import subprocess
import os
import shutil
import imageio_ffmpeg as ffmpeg

def file_manager(user_path):
    file_name = user_path.split("\\")[-1]
    try :
        shutil.copy(user_path, os.path.join("Video", file_name))
    except :
        files = os.listdir(user_path)
        for file in files :
            shutil.copy(os.path.join(user_path, file), os.path.join("Video", file))
        
def processor(input_file, output_file):
    exe = ffmpeg.get_ffmpeg_exe()
    subprocess.run([
    exe, "-i", os.path.join("Video", input_file),
    "-vn", "-acodec", "mp3", os.path.join("Audio", f"{output_file}.mp3")
    ])
