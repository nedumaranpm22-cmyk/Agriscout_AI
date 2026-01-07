import { useState } from "react";
import { analyzeImage } from "./api";

export default function App() {
  const [file, setFile] = useState(null);
  const [lang, setLang] = useState("en");
  const [answers, setAnswers] = useState([]);
  const [data, setData] = useState(null);

  const submit = async () => {
    if (!file) return;
    const res = await analyzeImage(file, lang, answers);
    setData(res);
  };

  return (
    <div style={{ maxWidth: 420, margin: "auto", padding: 20 }}>
      <h2>🌱 AgriScout</h2>

      <select onChange={e => setLang(e.target.value)}>
        <option value="en">English</option>
        <option value="ta">தமிழ்</option>
      </select>

      <input type="file" onChange={e => setFile(e.target.files[0])} />

      {data?.questions?.map((q, i) => (
        <div key={i}>
          <p>{q}</p>
          <button onClick={() => setAnswers([...answers, 1])}>Yes</button>
          <button onClick={() => setAnswers([...answers, 0])}>No</button>
        </div>
      ))}

      <button onClick={submit}>Analyze</button>

      {data && (
        <div>
          <h3>{data.prediction.class_name}</h3>
          <p>Confidence: {data.prediction.confidence * 100}%</p>
          <p>Risk: {data.risk}</p>

          <ul>
            {data.steps.map(step => <li key={step}>{step}</li>)}
          </ul>

          <p>{data.assistant_message}</p>
        </div>
      )}
    </div>
  );
}
