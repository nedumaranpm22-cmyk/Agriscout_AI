import { useState } from "react";
import { analyzeImage } from "./api";

export default function App() {
  const [file, setFile] = useState(null);
  const [lang, setLang] = useState("en");
  const [data, setData] = useState(null);
  const [answers, setAnswers] = useState([]);
  const [loading, setLoading] = useState(false);

  const submitImage = async () => {
    setLoading(true);
    setAnswers([]);
    const res = await analyzeImage(file, lang);
    setData(res);
    setLoading(false);
  };

  const submitAnswers = async () => {
    if (!data?.questions || answers.length !== data.questions.length) {
      alert(lang === "ta"
        ? "அனைத்து கேள்விகளுக்கும் பதிலளிக்கவும்"
        : "Please answer all questions");
      return;
    }

    setLoading(true);
    const res = await analyzeImage(file, lang, answers);
    setData(res);
    setLoading(false);
  };

  const setAnswer = (i, value) => {
    const a = [...answers];
    a[i] = value;
    setAnswers(a);
  };

  return (
    <div style={{ width: 540, margin: "auto", padding: 20 }}>
      <h2>🌱 AgriScout (Agentic AI)</h2>

      <select value={lang} onChange={e => setLang(e.target.value)}>
        <option value="en">English</option>
        <option value="ta">தமிழ்</option>
      </select>

      <br /><br />

      <input type="file" onChange={e => setFile(e.target.files[0])} />

      <br /><br />

      <button onClick={submitImage} disabled={loading}>
        {loading ? "Processing..." : "Analyze"}
      </button>

      {/* QUESTIONS */}
      {data?.mode === "questions" && (
        <div style={{ marginTop: 20 }}>
          <h3>{lang === "ta" ? "AI கேள்விகள்" : "AI Questions"}</h3>

          {data.questions.map((q, i) => (
            <div key={i} style={{ marginBottom: 12 }}>
              <p>{q}</p>

              <button
                style={{
                  backgroundColor: answers[i] === "yes" ? "#4CAF50" : "#eee",
                  marginRight: 10
                }}
                onClick={() => setAnswer(i, "yes")}
              >
                Yes
              </button>

              <button
                style={{
                  backgroundColor: answers[i] === "no" ? "#f44336" : "#eee"
                }}
                onClick={() => setAnswer(i, "no")}
              >
                No
              </button>
            </div>
          ))}

          <button onClick={submitAnswers} disabled={loading}>
            {loading
              ? "Processing..."
              : lang === "ta"
              ? "பதில்களை சமர்ப்பிக்கவும்"
              : "Submit Answers"}
          </button>
        </div>
      )}

      {/* ERROR SAFETY */}
      {data?.mode === "error" && (
        <div style={{ color: "red", marginTop: 20 }}>
          <strong>Error:</strong> {data.message}
        </div>
      )}

      {/* FINAL RESULT (ROBUST FALLBACK) */}
      {data?.prediction && data?.steps && (
        <div style={{ marginTop: 30 }}>
          <h3>{data.prediction.class_name}</h3>

          <p>
            {lang === "ta" ? "நம்பிக்கை" : "Confidence"}:{" "}
            {(data.prediction.confidence * 100).toFixed(2)}%
          </p>

          <p>
            {lang === "ta" ? "ஆபத்து நிலை" : "Risk"}: {data.risk}
          </p>

          <h4>{lang === "ta" ? "பாதுகாப்பு நடவடிக்கைகள்" : "Safety Steps"}</h4>
          <ul>
            {data.steps.map((s, i) => (
              <li key={i}>{s}</li>
            ))}
          </ul>

          {data.assistant_message && (
            <>
              <h4>{lang === "ta" ? "AI ஆலோசனை" : "AI Advice"}</h4>
              <p>{data.assistant_message}</p>
            </>
          )}
        </div>
      )}
    </div>
  );
}
