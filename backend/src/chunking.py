import json


def round_10(x):
    """Round x up to the next multiple of 10 (used to determine chunk boundaries)."""
    return x + (11 - x % 10)


def manage_chunk(file):
    """
    Groups Whisper transcript segments into fixed-size chunks of 10 segments each.

    Each chunk aggregates the text of 10 consecutive segments and records the
    overall start/end timestamps and video title. This balances context size
    (enough text for meaningful retrieval) with granularity (precise timestamps).
    """
    with open(f"Transcripted_json/{file}", "r") as f:
        data = json.loads(f.read())
    lst = []
    for i in range(10, round_10(len(data["chunks"])), 10):
        s = ""
        for j in range(i - 10, i):
            try:
                s += data["chunks"][j]["Text"]
            except Exception:
                s += ""
        try:
            lst.append({
                "Start": data["chunks"][j - 9]["Start"],  # type: ignore
                "End": data["chunks"][j]["End"],           # type: ignore
                "Video_title": data["chunks"][10]["Video_title"],
                "Text": s
            })
        except Exception:
            lst.append({
                "Start": data["chunks"][j - 9]["Start"],  # type: ignore
                "End": data["chunks"][len(data["chunks"]) - 1]["End"],
                "Video_title": data["chunks"][0]["Video_title"],
                "Text": s
            })

    with open(f"Managed_chunk/{file}", "w") as f:
        json.dump(lst, f)
