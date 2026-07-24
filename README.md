# AI Chat API + Web Chat Interface

## Overview

This project is developed for the **OS3 AI Engineer Technical Evaluation (L1-02)**.

It is a FastAPI-based AI chatbot application integrated with the **Google Gemini API**. The application provides REST APIs, session-based conversation memory, and a modern web chat interface.

---

## Features

- FastAPI Backend
- REST APIs
- Google Gemini API Integration
- Session-Based Conversation Memory
- Modern Chat UI
- Health Check Endpoint
- JSON Responses
- Environment Variable Configuration

---

## Folder Structure

```
AI-Assignment-Set1-L1-02/

├── app/
│   ├── __init__.py
│   ├── chatbot.py
│   ├── config.py
│   ├── main.py
│   ├── memory.py
│   ├── models.py
│   └── routes.py
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── requirements.txt
├── README.md
├── run.py
├── .env.example
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>

cd AI-Assignment-Set1-L1-02
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
MODEL_NAME=gemini-2.5-flash
```

---

## Run Application

```bash
python run.py
```

Application URL

```
http://localhost:8000
```

---

## API Endpoints

### Health Check

```
GET /health
```

Response

```json
{
  "status": "healthy",
  "service": "AI Chat API"
}
```

---

### Chat API

```
POST /chat
```

Request

```json
{
  "session_id": "123",
  "message": "Hello"
}
```

Response

```json
{
  "reply": "Hello! How can I help you?",
  "session_id": "123"
}
```

---

## Technologies Used

- Python
- FastAPI
- Google Gemini API
- HTML
- CSS
- JavaScript
- Jinja2
- Pydantic
- Python Dotenv

---

## Future Improvements

- Persistent Database Storage
- User Authentication
- Streaming Responses
- Conversation Export
- Docker Support

---

## Author

**Gaurav Kuvar**

OS3 AI Engineer Technical Evaluation – Set 1 (L1-02)
