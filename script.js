// عند رفع الفيديو
document.getElementById('videoUpload').addEventListener('change', async function(e) {
    const file = e.target.files[0];
    const videoPlayer = document.getElementById('videoPlayer');
    
    if (file) {
        videoPlayer.src = URL.createObjectURL(file);
        document.getElementById('videoContainer').style.display = 'block';
        
        // إرسال الفيديو إلى السيرفر
        const formData = new FormData();
        formData.append('video', file);
        
        try {
            const response = await fetch('https://your-server.com/upload', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            document.getElementById('translatedText').textContent = result.text;
            document.getElementById('resultContainer').style.display = 'block';
        } catch (error) {
            alert("حدث خطأ أثناء التحليل");
        }
    }
});
