فهمت! تريد **نسخة مبسطة من السيرڤر بدون استخدام الذكاء الاصطناعي**، فقط لإنشاء هيكل أساسي لرفع الفيديو وعرض نتائج وهمية. إليك الكود:

### 📜 ملف `app.py` (بدون AI - للتدريب فقط)
```python
from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)

# واجهة HTML مع JS مدمج
HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>نموذج تجريبي</title>
    <style>
        body { font-family: Arial; text-align: center; margin-top: 50px; }
        button { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
        #result { margin-top: 20px; padding: 15px; background: #f8f9fa; display: none; }
    </style>
</head>
<body>
    <h1>نموذج لرفع الفيديو (بدون تحليل)</h1>
    <input type="file" id="videoInput" accept="video/*">
    <button onclick="uploadVideo()">رفع الفيديو</button>
    <div id="result">
        <p id="demoText">هذا نص تجريبي للعرض فقط!</p>
    </div>

    <script>
        function uploadVideo() {
            const file = document.getElementById('videoInput').files[0];
            if (!file) return alert("اختر فيديو أولاً");
            
            // محاكاة إرسال الفيديو للسيرڤر (بدون تحليل حقيقي)
            document.getElementById('result').style.display = 'block';
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)
```

### كيفية التشغيل:
1. احفظ الكود في ملف `app.py`.
2. افتح الترمينال في نفس المجلد.
3. اكتب:
   ```bash
   python app.py
   ```
4. افتح المتصفح على:
   ```
   http://localhost:5000
   ```

### ماذا يفعل هذا الكود؟
- يعرض واجهة بسيطة لرفع الفيديو.
- **لا يحلل الفيديو** (يظهر نصًا ثابتًا فقط).
- مثالي لفهم هيكل السيرڤر قبل إضافة الذكاء الاصطناعي.

إذا كنت تريد إضافة مميزات محددة أخبرني! 😊
