# Agentic AI Tutorials

Hands-on tutorials and labs for building local agentic AI applications with Ollama, Gradio, and notebook-based exercises using Qwen and Llama model tracks.

## GitHub Description

Hands-on Agentic AI tutorials and labs with local Ollama models, Gradio chat apps, and Qwen/Llama notebook tracks.

## Project Overview

This repository is designed as a practical learning workspace for agentic AI development. It includes:

- A working local chat application powered by Ollama and Gradio
- Notebook labs for Qwen model tracks
- Cross-platform setup guides for macOS, Linux, and Windows (WSL2)
- Personal-agent examples that demonstrate tool calling and memory-style context injection

## Key Features

- Local-first LLM workflows with Ollama
- Interactive Gradio chat interface
- Function/tool-calling patterns in Python
- Structured lab progression through Jupyter notebooks


## Repository Structure

```text
.
├── ollama_chat.py
├── pyproject.toml
├── requirements.txt
├── setup_mac.md
├── setup_linux.md
├── setup_windows.md
├── personal-agent-qwen/
│   ├── lab1_qwen.ipynb
│   ├── lab2_qwen.ipynb
│   └── lab3_qwen.ipynb
├── assets/
│   └── logo.png
└── me/
    └── summary.txt
```

## Prerequisites

1. Python 3.8+
2. Ollama installed and running locally
3. A downloaded Ollama model (for example, `qwen3:8b`)

For platform-specific setup instructions:

- macOS: `setup_mac.md`
- Linux: `setup_linux.md`
- Windows (WSL2): `setup_windows.md`

## Installation

1. Clone this repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start Ollama service if it is not already running:

```bash
ollama serve
```

4. Pull at least one model:

```bash
ollama pull qwen3:8b
```

## Run the Chat App

Start the Gradio app:

```bash
python ollama_chat.py
```

Then open the local URL shown in terminal output (typically `http://127.0.0.1:7860`).

## Configuration

In `ollama_chat.py`, update the model name as needed:

```python
model_name = "qwen3:8b"
```

You can switch to any model available in your local Ollama library.

## Learning Path

Suggested order:

1. Complete environment setup for your OS
2. Run `ollama_chat.py` to validate local inference
3. Work through `personal-agent-qwen/lab1_qwen.ipynb` to `lab3_qwen.ipynb`
4. Continue with `assets/personal-agent-llama/lab1_llama.ipynb` to `lab3.ipynb`

## Tech Stack

- Python
- Ollama
- Gradio
- OpenAI-compatible client patterns
- Jupyter Notebooks

## Notes

- Some examples use local files from the `me/` directory for context-driven responses.
- If a model is unavailable locally, pull it first using `ollama pull <model-name>`.

## License

Add your preferred license information here.
