import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import requests as req
import numpy as np
import shutil
import os

def embed_factory(l):
    r = req.post(url="http://localhost:11434/api/embed", json={"model" : "bge-m3", "input" : l})
    return r.json()["embeddings"]

def prompt(file_name, user_query, test=None, test_path=None):
    try:
        if test:
            shutil.copy(test_path, os.path.join("saved_parquets", f"{file_name}.parquet"))  #type: ignore
    except Exception as e:
        print(e)
    try :
        db = pd.read_parquet(f"parquet_files/{file_name}.parquet")
    except :
        db = pd.read_parquet(f"saved_parquets/{file_name}.parquet")
    response = cosine_similarity(np.vstack(db["embedding"]), embed_factory(user_query)).flatten().argsort()[::-1][:3] #type: ignore
            
    df = db.loc[response]

    prompt = f'''help the user with the data given below that contains Video number, starting point in seconds, ending point in seconds and the text between starting point and ending point :
    {df[["Video_title", "Start", "End", "Text"]].to_json(orient="records")}
    ---------------------------------
    "{user_query}"
    User asked this question related to the video chunks, you have to answer in a human way (dont mention the above format, its just for you). At the end, guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer questions related to the chunks.
    '''
    return prompt

def inference(prompt, model_for_output):
    r = req.post("http://localhost:11434/api/generate", json={
        "model": model_for_output,
        "prompt": prompt,
        "stream": False
    })
    response = r.json()
    return response["response"]


