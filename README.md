# VideoMind — Video Question Answering System (RAG-based)

## 📌 Description

**VideoMind** lets you ask questions about video content in plain English.

It accepts a single video file, a folder containing multiple videos, or a pre-built `.parquet` vector database as input. The video is processed through a RAG (Retrieval-Augmented Generation) pipeline — speech is transcribed with Whisper, chunked, embedded with `bge-m3`, and then queried using an Ollama-hosted LLM.

-----------------------------------------------------------------------------------------------------------------

## ✨ Main Features

- Accepts **single video files**, **folders with multiple videos**, or **parquet vector databases** as input
- Automatically extracts audio and transcribes speech with **OpenAI Whisper**
- Uses **Retrieval-Augmented Generation (RAG)** with `bge-m3` embeddings for accurate, context-aware responses
- Generates answers with any **Ollama-hosted LLM** (default: `qwen3:4b`)
- Provides **timestamp references** so you know exactly where in the video the answer comes from
- Clean **PySide6 desktop UI** with light/dark theme, settings dialog, and background processing
- Modular and extensible pipeline

-----------------------------------------------------------------------------------------------------------------

## 🧠 How It Works

```
Video File(s)
    │
    ▼
Audio Extraction  (FFmpeg via imageio-ffmpeg)
    │
    ▼
Speech-to-Text    (OpenAI Whisper)
    │
    ▼
Chunking          (10-segment windows with timestamps)
    │
    ▼
Embeddings        (bge-m3 via Ollama)
    │
    ▼
Vector Store      (Parquet + cosine similarity)
    │
    ▼
LLM Answer        (qwen3:4b or any Ollama model)
```

-----------------------------------------------------------------------------------------------------------------

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| UI | PySide6 |
| Speech-to-Text | OpenAI Whisper |
| Embedding Model | bge-m3 (via Ollama) |
| LLM | qwen3:4b (via Ollama, configurable) |
| Audio Extraction | FFmpeg (via imageio-ffmpeg) |
| Vector Store | Parquet (pandas + pyarrow) |
| Retrieval | scikit-learn cosine similarity |
| Language | Python |

-----------------------------------------------------------------------------------------------------------------

# ⚙️ Installation

## Step 1. Clone the repository

```bash
git clone https://github.com/Dominator930/VideoMind.git
cd VideoMind
```

-----------------------------------------------------------------------------------------------------------------

## Step 2. Install requirements

Requires **Python 3.10+**. Create a virtual environment, then install:

```bash
pip install -r requirements.txt
```

> **Note:** `torch` (pulled in by Whisper) is large. The default pip install is CPU-friendly. For a CUDA build, install the matching torch wheel from [pytorch.org](https://pytorch.org/) before or after `requirements.txt`.

-----------------------------------------------------------------------------------------------------------------

## Step 3. Install Ollama and pull the required models

Visit [https://ollama.com/](https://ollama.com/), download and install Ollama, then open a terminal and run:

```bash
# Embedding model (required)
ollama pull bge-m3

# LLM output model (default — or replace with any model you prefer)
ollama pull qwen3:4b
```

> **Note:** You can change both the Whisper model size and the Ollama output model from the **Settings (⚙)** dialog inside the app.

-----------------------------------------------------------------------------------------------------------------

## Step 4. Run the project

```bash
python app.py
```

-----------------------------------------------------------------------------------------------------------------

## 📝 Notes

- **Parquet reuse:** After processing a video, the pipeline saves a `.parquet` vector database to `backend/src/saved_parquets/`. You can load it directly next time instead of reprocessing the video — just select it at the file picker.
- **Multiple videos:** Select a folder containing multiple video files; all will be processed and merged into a single searchable database.
- **Model size vs. speed:** The default Whisper model is `medium`. Switch to `base` or `tiny` for faster processing on lower-end systems, or `large-v3` for best accuracy (especially for non-English content).
- **Ollama must be running** before launching VideoMind (it starts automatically on most systems after install).
- **Health check (optional):** Place a `.parquet` or video under `backend/test/test_subjects/`, then run `python -m backend.test.test`. Skips cleanly if that folder is missing.
