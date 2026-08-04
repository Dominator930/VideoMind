import requests as req
import pandas as pd


def embed_factory(l:list):
    r = req.post(url="http://localhost:11434/api/embed", json={"model" : "bge-m3", "input" : l})
    return r.json()["embeddings"]


def create_db(file_name):
    lst = []
    df = pd.read_parquet("parquet_files/all_saved_chunks.parquet")
    for i in df["Text"]:
        lst.append(i)  
    lst = embed_factory(lst)
    df["embedding"] = lst
    df.to_parquet(f"parquet_files/{file_name}.parquet")
