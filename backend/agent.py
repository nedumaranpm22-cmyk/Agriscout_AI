QUESTIONS = {
    "en": [
        "Are the spots spreading to other leaves?",
        "Are multiple leaves affected?",
        "Has the condition worsened recently?"
    ],
    "ta": [
        "இந்த புள்ளிகள் மற்ற இலைகளுக்கும் பரவுகிறதா?",
        "ஒரே செடியில் பல இலைகள் பாதிக்கப்பட்டுள்ளதா?",
        "கடந்த நாட்களில் பாதிப்பு அதிகரித்ததா?"
    ]
}

def decide_risk(answers_score):
    if answers_score >= 2:
        return "HIGH"
    elif answers_score == 1:
        return "MEDIUM"
    else:
        return "LOW"

def get_questions(lang="en"):
    return QUESTIONS[lang]
