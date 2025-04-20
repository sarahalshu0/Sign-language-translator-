document.getElementById('uploadBtn').addEventListener('click', async () => {
    const file = document.getElementById('videoInput').files[0];
    if (!file) return alert("يرجى اختيار فيديو");

    const formData = new FormData();
    formData.append('video', file);

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        
        document.getElementById('outputText').textContent = data.text;
        document.getElementById('results').style.display = 'block';
    } catch (error) {
        alert("حدث خطأ أثناء التحليل");
    }
});
