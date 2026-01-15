from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from agent import agriscout_agent
import traceback

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AgriScout backend running"

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        lang = request.form.get("lang", "en")
        answers = request.form.getlist("answers[]")

        if "image" not in request.files:
            return jsonify({"error": "Image missing"}), 400

        image = Image.open(request.files["image"])

        result = agriscout_agent(
            image=image,
            lang=lang,
            answers=answers if answers else None
        )

        return jsonify(result)

    except Exception as e:
        print("🔥 BACKEND ERROR 🔥")
        traceback.print_exc()

        return jsonify({
            "mode": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
