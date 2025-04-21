from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    video = request.files['video']
    video.save('temp.mp4')

    # TODO: استبدال هذا النص بالناتج الفعلي من نموذج الذكاء
    result_text = "هذه محاكاة لتحليل لغة الإشارة من الفيديو."

    return jsonify({'text': result_text})

if __name__ == '__main__':
    app.run(debug=True)