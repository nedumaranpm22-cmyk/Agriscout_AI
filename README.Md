# 🌱 AgriScout AI
### _Agentic Crop Disease Detection & Safe Farming Assistant_

---

## 🧠 Overview

**AgriScout AI** is an AI-powered web application that helps farmers detect crop diseases using **leaf images** and provides **safe, guideline-based recommendations**.

The system combines **computer vision (MobileNetV3)** with **agentic AI reasoning** and **Gemini LLM** to deliver **explainable**, **bilingual (English & Tamil)**, and **farmer-safe** guidance.
## 🚀 Features

- 📸 Image-based crop disease detection using **MobileNetV3 (PyTorch)**
- 🧠 Agentic AI assistant that decides when to ask clarifying questions
- 📊 Confidence-aware questioning for reliable results
- 🛡️ Safety-first design (no chemical / medical advice)
- 🌐 Bilingual support (**English & Tamil**)
- 📱 Mobile-first responsive React UI
- ⚡ Flask backend API for inference & agent logic
- 🔒 Safe LLM explanations using **Gemini**
## 🧩 System Architecture

```plaintext
Frontend (React)
     ↓
Backend (Flask API)
     ↓
Model (MobileNetV3 - PyTorch)
     ↓
Agent Logic (Confidence + Risk Analysis)
     ↓
Gemini LLM (Safe Explanation)

---

## PART 4 — Tech Stack

```markdown
## 🛠️ Tech Stack

| Component | Technology |
|---------|------------|
| Frontend | React JS |
| Backend | Flask (Python) |
| AI / ML Model | MobileNetV3 (PyTorch) |
| LLM Integration | Gemini Flash |
| Image Processing | Pillow |
| Database (Optional) | SQLite / JSON Logs |
## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/agriscout-ai.git
cd agriscout-ai

---

## PART 6 — Backend Setup

```markdown
### 2️⃣ Backend Setup

```bash
cd backend
python3 -m venv venv
# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
pip install -r requirements.txt
python app.py

---

## PART 7 — Frontend Setup

```markdown
### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start

---

## PART 8 — Environment Variables

```markdown
## 🔐 Environment Variables

Create a `.env` file inside the **backend** folder:

```env
GEMINI_API_KEY=your_gemini_api_key_here

---

## PART 9 — API Reference

```markdown
## 📡 API Reference

### Endpoint
```http
POST /analyze

---

## PART 10 — API Parameters & Response

```markdown
### Request Parameters

| Field | Type | Description |
|------|------|------------|
| image | file | Leaf image for analysis |
| language | string | `en` or `ta` |
| answers[] | array (optional) | Clarifying questionnaire answers |

---

### Sample Response

```json
{
  "prediction": {
    "class": "Tomato___Leaf_Spot",
    "confidence": 0.87
  },
  "questions": [
    "Do you see yellow spots on the leaf edges?"
  ],
  "risk": "medium",
  "steps": [
    "Keep the leaves dry",
    "Ensure proper sunlight"
  ],
  "assistant_message": "It seems like a mild fungal issue. Avoid excess watering."
}
## 🛡️ Safety Rules

- ❌ No pesticide or chemical recommendations
- ❌ No medical treatment suggestions
- ✅ Only safe, general agricultural guidelines
- 👨‍🌾 Encourage consultation with certified experts
## 🌍 Languages Supported

- English (`en`)
- Tamil (`ta`)
## 📁 Project Structure

```plaintext
agriscout/
│
├── backend/
│   ├── app.py
│   ├── model_loader.py
│   ├── inference.py
│   ├── agent.py
│   ├── safety_rules.py
│   ├── class.json
│   ├── mobilenetv3_epoch1.pth
│   └── requirements.txt
│
├── frontend/
│   └── src/
│       ├── App.js
│       ├── api.js
│       ├── index.css
│       └── components/
│
└── README.md

---

## PART 15 — Deployment

```markdown
## 🚀 Deployment (Optional)

### Backend
- Render
- Railway
- Hugging Face Spaces

### Frontend
- Vercel
- Netlify
## 💡 Future Improvements

- 📊 Real-time crop monitoring dashboard
- 🏛️ Government agriculture API integration
- 🔁 Automated model retraining pipeline
## 🤝 Contributors

- **Nedumaran** – Project Lead & Developer  
- *Your Team / College Name* (optional)
## 🧾 License

This project is licensed under the **MIT License**.

> Use responsibly — for educational and research purposes only.

---

## 🌾 Acknowledgements

Special thanks to:

- Google Gemini AI
- PyTorch Team
- Open-source AgriML datasets
- Farmers who inspire tech innovation ❤️

---

> **“Empowering farmers through responsible AI — because safer crops mean a safer future.” 🌱**

