import google.generativeai as genai

from app.config import GEMINI_API_KEY, MODEL_NAME

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(MODEL_NAME)

def ask_llm(history):
    prompt = ""

    for msg in history:
        prompt += f"{msg['role']}: {msg['content']}\n"

    response = model.generate_content(prompt)

    return response.text
