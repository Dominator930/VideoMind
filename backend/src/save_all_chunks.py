import pandas as pd
import json

def save_chunk(files):
    all_df = []
    for file in files:
        if not file.endswith(".gitkeep"):
            with open(f"Managed_chunk/{file}", "r") as f:
                data = json.loads(f.read())
            df = pd.DataFrame().from_records(data)
            all_df.append(df)
        
    df = pd.concat(all_df, ignore_index=True)

    df.to_parquet("parquet_files/all_saved_chunks.parquet")
    
    