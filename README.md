# 🤖 AI ChatBot

A web-based chatbot powered by Flask and Ollama.

## Features

- AI conversations using Mistral
- Modern UI
- File upload support
- PDF summarization
- Local execution with Ollama

## Technologies

- Python
- Flask
- HTML
- CSS
- JavaScript
- Ollama
- Mistral

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Install the model:

```bash
ollama pull mistral
```

Start Ollama:

```bash
ollama serve
```

Run the application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Architecture

```text
User
 ↓
JavaScript
 ↓
Flask
 ↓
Ollama
 ↓
Mistral
 ↓
Flask
 ↓
JavaScript
 ↓
Response
```

## What I Learned

- Flask development
- REST APIs
- Frontend/backend communication
- JavaScript Fetch API
- Local LLM deployment with Ollama
- Git & GitHub

## Author

Mohamed Omar Ben Hammouda
