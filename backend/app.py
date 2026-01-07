import os
import logging
from flask import Flask, request, jsonify
try:
    from flask_cors import CORS
except Exception:
    # CORS is optional for local testing; continue without it if missing
    CORS = None
from PIL import Image

from model_loader import load_model
from inference import predict
from agent import decide_risk, get_questions
from safety_rules import safe_steps

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
if CORS:
    CORS(app)

# Load ML model (fail gracefully if torch or weights are unavailable)
try:
    model = load_model("mobilenetv3_epoch1.pth")
except Exception as e:
    logging.warning("Model could not be loaded: %s", e)
    model = None

@app.route("/analyze", methods=["POST"])
def analyze():
    image_file = request.files.get("image")
    lang = request.form.get("language", "en")
    answers = request.form.getlist("answers[]") or []

    # Image inference (if model available)
    if image_file is None:
        return jsonify({"error": "no image provided"}), 400

    image = Image.open(image_file).convert("RGB")
    if model is None:
        prediction = {"error": "model not loaded"}
    else:
        prediction = predict(model, image)

    # Agent reasoning
    score = sum(int(a) for a in answers) if answers else 0
    risk = decide_risk(score)

    # Gemini explanation (SAFE USE)
    prompt = f"""
You are an agricultural assistant.

Explain the following safely for a farmer.
Language: {'Tamil' if lang=='ta' else 'English'}
Risk level: {risk}

Rules:
- Do NOT suggest chemicals
- Do NOT add new advice
- Be calm and supportive
"""

    # Gemini explanation (optional) — use environment variable `GENAI_API_KEY`
    assistant_message = None
    api_key = os.environ.get("GENAI_API_KEY")
    if api_key:
        try:
            # import lazily so app can run without the genai package installed
            from google import genai
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model="models/gemini-1.0-pro",
                contents=prompt
            )
            assistant_message = getattr(response, "text", None)
        except Exception as e:
            logging.warning("Generative AI call failed: %s", e)
            assistant_message = None

    return jsonify({
        "prediction": prediction,
        "questions": get_questions(lang),
        "risk": risk,
        "steps": safe_steps(risk, lang),
        "assistant_message": assistant_message
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
