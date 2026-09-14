import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import requests as req
import numpy as np
import shutil
import os
from .config import embed_model


def embed_factory(l):
    r = req.post(url="http://localhost:11434/api/embed", json={"model": embed_model, "input": l})
    return r.json()["embeddings"]


def prompt(file_name, user_query, test=None, test_path=None):
    try:
        if test:
            shutil.copy(test_path, os.path.join("saved_parquets", f"{file_name}.parquet"))  # type: ignore
    except Exception as e:
        print(e)
    try:
        db = pd.read_parquet(f"parquet_files/{file_name}.parquet")
    except Exception:
        db = pd.read_parquet(f"saved_parquets/{file_name}.parquet")

    response = cosine_similarity(np.vstack(db["embedding"]), embed_factory(user_query)).flatten().argsort()[::-1][:3]  # type: ignore

    df = db.loc[response]
    prompt_text = f'''help the user with the data given below that contains Video title, starting point in seconds, ending point in seconds which you will convert to hour, minutes, seconds format if applicable and the text between starting point and ending point :
    {df[["Video_title", "Start", "End", "Text"]].to_json(orient="records")} absolutely do not mention anything about this data it's just for you.
    ---------------------------------
    "{user_query}"
    User asked this question related to the video chunks, you have to answer in a human way (dont mention this format as well, its just for you). At the end, tell the user about the exact timestamp in video/videos which contains related information asked by the user. If user asks unrelated question, tell him that you can only answer questions related to the chunks.
    '''
    return prompt_text


def inference(prompt, model_for_output):
    r = req.post("http://localhost:11434/api/generate", json={
        "model": model_for_output,
        "prompt": prompt,
        "stream": False
    })
    response = r.json()
    return response["response"]
