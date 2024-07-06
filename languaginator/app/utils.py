import os
from openai import OpenAI
from sqlalchemy.orm import Session
from app.crud import update_translation_task

from app.config import Config


openai = OpenAI(api_key=Config.OPENAI_API_KEY)


def perform_translation(task_id: int, text: str, languages: list[str], db: Session):
    translations = {}

    for lang in languages:
        try:
            response = openai.chat.completions.create(
                model="davinci-002",
                messages=[
                    {
                        "role": "system",
                        "content": f"You are an helpful assistant that translates text into {lang} language",
                    },
                    {"role": "user", "content": text},
                ],
                max_tokens=1000,
            )

            translated_text = response["choices"][0]["message"]["content"].strip()

            translations[lang] = translated_text
        except Exception as e:
            print(f"Error translating to {lang} : {e}")
            translations[lang] = f"Error: {e}"

    update_translation_task(db, task_id, translations)
