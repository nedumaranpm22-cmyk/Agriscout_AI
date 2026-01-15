def get_steps(risk, lang):
    rules = {
        "HIGH": {
            "en": [
                "Avoid chemicals",
                "Limit field movement",
                "Consult agriculture officer"
            ],
            "ta": [
                "ரசாயனங்களை தவிர்க்கவும்",
                "புலத்தில் இயக்கத்தை குறைக்கவும்",
                "வேளாண் அலுவலரை அணுகவும்"
            ]
        },
        "MEDIUM": {
            "en": [
                "Remove affected leaves",
                "Improve air circulation",
                "Observe for 3–5 days"
            ],
            "ta": [
                "பாதிக்கப்பட்ட இலைகளை அகற்றவும்",
                "காற்றோட்டத்தை மேம்படுத்தவும்",
                "3–5 நாட்கள் கவனிக்கவும்"
            ]
        }
    }
    return rules[risk][lang]
