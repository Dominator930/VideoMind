import json
import whisper

def transformer(file, model):
    model = whisper.load_model(model)
    file_name = "".join(file.split(".")[0:-1])
    chunks = []
    result = model.transcribe(audio = f"Audio/{file}")
    for segment in result["segments"]:
        chunks.append({"Start": segment["start"], "End": segment["end"], "Text": segment["text"], "Video_title": f"{file_name}"})       #type: ignore
    chunks_with_metadata = {"chunks": chunks, "text": result["text"]}
    with open(f"Transcripted_json/{file_name}.json", "w") as f: 
        json.dump(chunks_with_metadata, f)

        