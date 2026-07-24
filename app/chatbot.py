from openai import OpenAI

from app.config import OPENAI_API_KEY
from app.config import MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)


def ask_llm(history):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=history,
        temperature=0.5
    )

    return response.choices[0].message.content
