# AI Chat API + Web Chat Interface

## Overview

This project is developed for OS3 AI Engineer Evaluation (L1-02).

Features

- FastAPI Backend
- REST APIs
- OpenAI Chat Integration
- Session Memory
- Modern Chat UI
- Health Check Endpoint
- JSON Responses

---

## Folder Structure

```
AI-Assignment-Set1-L1-02

app/
static/
templates/
run.py
requirements.txt
README.md
.env.example
```

---

## Installation

```bash
git clone <repository-url>

cd AI-Assignment-Set1-L1-02

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## Configure Environment

Create .env

```
OPENAI_API_KEY=YOUR_KEY
MODEL_NAME=gpt-4o-mini
```

---

## Run

```
python run.py
```

Server

```
http://localhost:8000
```

---

## API

### GET

```
/health
```

Returns

```json
{
 "status":"healthy"
}
```

---

### POST

```
/chat
```

Example

```json
{
 "session_id":"123",
 "message":"Hello"
}
```

Response

```json
{
 "reply":"Hello! How can I help you?"
}
```

---

## Technologies

- Python
- FastAPI
- HTML
- CSS
- JavaScript
- OpenAI API

---

## Author

Gaurav Kuvar
