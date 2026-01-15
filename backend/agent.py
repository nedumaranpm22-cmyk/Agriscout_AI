from inference import predict
from safety_rules import get_steps
from llm import ask_llm

# AGENTIC QUESTIONS (ALWAYS ASKED)
QUESTIONS = {
    "en": [
        "Are more than 25% of plants affected?",
        "Has there been heavy rain recently?",
        "Is this crop in early growth stage?"
    ],
    "ta": [
        "25%க்கும் மேற்பட்ட பயிர்கள் பாதிக்கப்பட்டுள்ளதா?",
        "சமீபத்தில் அதிக மழை பெய்ததா?",
        "பயிர் ஆரம்ப வளர்ச்சி நிலையிலா உள்ளது?"
    ]
}

def agriscout_agent(image, lang, answers=None):
    prediction = predict(image)
    risk = "HIGH" if prediction["confidence"] > 0.7 else "MEDIUM"

    # STEP 1: ALWAYS ASK QUESTIONS
    if answers is None:
        return {
            "mode": "questions",
            "prediction": prediction,
            "questions": QUESTIONS[lang]
        }

    # STEP 2: FINAL DECISION AFTER ANSWERS
    clean_answers = [
        "ஆம்" if a == "yes" and lang == "ta" else
        "இல்லை" if a == "no" and lang == "ta" else
        "Yes" if a == "yes" else
        "No"
        for a in answers
    ]

    steps = get_steps(risk, lang)

    advice = ask_llm(
        prediction["class_name"],
        risk,
        clean_answers,
        lang
    )

    return {
        "mode": "final",
        "prediction": prediction,
        "risk": risk,
        "steps": steps,
        "assistant_message": advice
    }
