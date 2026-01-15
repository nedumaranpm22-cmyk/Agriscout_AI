import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def ask_llm(disease, risk, answers, lang):
    # Fallback message (VERY IMPORTANT)
    if lang == "ta":
        fallback = (
            f"பயிரில் {disease} நோய் கண்டறியப்பட்டுள்ளது. "
            f"ஆபத்து நிலை: {risk}. "
            "மேலே குறிப்பிடப்பட்ட பாதுகாப்பு நடவடிக்கைகளை பின்பற்றவும்."
        )
    else:
        fallback = (
            f"The crop is affected by {disease}. "
            f"Risk level: {risk}. "
            "Please follow the recommended safety steps."
        )

    try:
        prompt = (
            f"Disease: {disease}\n"
            f"Risk: {risk}\n"
            f"Farmer answers: {answers}\n\n"
            "Give clear, practical advice for the farmer."
        )

        res = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4o-mini",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3
            },
            timeout=20
        )

        data = res.json()

        # 🔑 CRITICAL GUARD
        if "choices" not in data or not data["choices"]:
            return fallback

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("LLM ERROR:", e)
        return fallback
