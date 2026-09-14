model = "medium"
# Whisper speech-to-text model size. Options:
#   "tiny"     — fastest, lowest accuracy
#   "base"     — fast, lower accuracy (good for low-end systems)
#   "small"    — balanced
#   "medium"   — recommended default
#   "large-v3" — highest accuracy, very slow (best for non-English content)

output_model = "qwen3:4b"
# The Ollama LLM used to generate answers. Any model you have pulled via
# `ollama pull <model_name>` can be used here.
# Examples: "llama3.2", "mistral", "gemma3", "qwen3:4b"
# Make sure Ollama is running before starting VideoMind.

embed_model = "bge-m3"
# The Ollama embedding model used to create the vector database.
# Pull it with: ollama pull bge-m3
# Changing this requires re-processing any existing videos.
