export async function analyzeImage(file, lang, answers) {
  const form = new FormData();
  form.append("image", file);
  form.append("language", lang);
  answers.forEach(a => form.append("answers[]", a));

  const res = await fetch("http://localhost:5000/analyze", {
    method: "POST",
    body: form
  });
  return res.json();
}
