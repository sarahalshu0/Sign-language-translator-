// static/script.js
document.getElementById('uploadForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);

  const response = await fetch('/analyze', {
    method: 'POST',
    body: formData
  });

  const data = await response.json();
  document.getElementById('result').value = data.text;
});

function speakText() {
  const text = document.getElementById('result').value;
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = 'ar-SA';
  speechSynthesis.speak(utterance);
}