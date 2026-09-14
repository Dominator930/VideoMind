import shutil
import os

def delete_files_and_create_parquet(file_name=None):
    try:
        base_dir = os.path.abspath(os.path.dirname(__file__))
        parquet_dir = os.path.join(base_dir, "parquet_files")
        saved_dir = os.path.join(base_dir, "saved_parquets")
        os.makedirs(saved_dir, exist_ok=True)

        if file_name:
            src = os.path.join(parquet_dir, f"{file_name}.parquet")
            dst = os.path.join(saved_dir, f"{file_name}.parquet")
            if os.path.exists(src):
                try:
                    shutil.move(src, dst)
                except Exception as e:
                    print(f"[Cleanup Error] Could not move parquet: {e}")

        folders = ["Audio", "Video", "Transcripted_json", "Managed_chunk", "parquet_files"]
        for folder in folders:
            folder_path = os.path.join(base_dir, folder)
            if os.path.exists(folder_path):
                for file in os.listdir(folder_path):
                    if not file.endswith(".gitkeep"):
                        try:
                            file_path = os.path.join(folder_path, file)
                            if os.path.isfile(file_path):
                                os.remove(file_path)
                        except Exception:
                            pass
    except Exception as e:
        print(f"[Cleanup Error] {e}")

    
def eval_func(test, path, vdo_2_aud_func, chunking_func, embeds_func, prompt_func, save_all_chunks_func, transcription_func):   
    if test:
        if not path.endswith(".parquet"):  
            if vdo_2_aud_func:
                print("[✓] vdo_2_aud.py")
            else :
                print("[✗] vdo_2_aud.py")
            if chunking_func:
                print("[✓] chunking.py")
            else :
                print("[✗] chunking.py")
            if embeds_func:
                print("[✓] embeds.py")
            else :
                print("[✗] embeds.py")
            if prompt_func:
                print("[✓] prompt.py")
            else :
                print("[✗] prompt.py")
            if save_all_chunks_func:
                print("[✓] save_all_chunks.py")
            else :
                print("[✗] save_all_chunks.py")
            if transcription_func:
                print("[✓] transcription.py")
            else :
                print("[✗] transcription.py")
                        
            if vdo_2_aud_func and transcription_func and prompt_func and save_all_chunks_func and chunking_func and embeds_func :
                print("Status: ALL TESTS PASSED ✓")
            else :
                print("Status: TEST FAILED ✗")
        else :
            if prompt_func:
                print("[✓] prompt.py")
            else :
                print("[✗] prompt.py")    

    