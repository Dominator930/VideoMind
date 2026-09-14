from pathlib import Path
import sys
import os

if __package__ in (None, ""):
    repository_root = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(repository_root))

from backend.src.main import Main

user_path = Path(__file__).parent / "test_subjects"

if not user_path.is_dir():
    print(
        "[Skip] backend/test/test_subjects/ not found.\n"
        "Place a .parquet (or video) file there to run the health check.\n"
        "Ollama must be running with bge-m3 and your configured LLM pulled."
    )
    sys.exit(0)

for i in os.listdir(user_path):
    if i.endswith(".parquet"):
        user_path = Path(__file__).parent / "test_subjects" / i
        break

file_name = user_path.name

test_obj = Main(str(user_path), file_name, True)

if __name__ == "__main__":
    test_obj.main_func()
