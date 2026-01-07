def safe_steps(risk, lang="en"):
    rules = {
        "LOW": {
            "en": [
                "Continue regular monitoring",
                "Ensure proper watering"
            ],
            "ta": [
                "தொடர்ந்து கண்காணிக்கவும்",
                "சரியான பாசனத்தை உறுதி செய்யவும்"
            ]
        },
        "MEDIUM": {
            "en": [
                "Remove affected leaves carefully",
                "Improve air circulation",
                "Observe for 3–5 days"
            ],
            "ta": [
                "பாதிக்கப்பட்ட இலைகளை கவனமாக அகற்றவும்",
                "காற்றோட்டத்தை மேம்படுத்தவும்",
                "3–5 நாட்கள் கண்காணிக்கவும்"
            ]
        },
        "HIGH": {
            "en": [
                "Avoid applying chemicals on your own",
                "Limit field movement",
                "Consult agriculture officer"
            ],
            "ta": [
                "தானாகவே ரசாயனங்களை பயன்படுத்த வேண்டாம்",
                "பயிர் புலத்தில் இயக்கத்தை குறைக்கவும்",
                "வேளாண் அலுவலரை தொடர்பு கொள்ளவும்"
            ]
        }
    }
    return rules[risk][lang]
