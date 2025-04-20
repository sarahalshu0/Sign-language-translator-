from flask import Flask, request, jsonify
import cv2
import mediapipe as mp
import numpy as np

app = Flask(__name__)

# تهيئة MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({"error": "No video uploaded"}), 400
    
    video = request.files['video']
    video.save('temp.mp4')
    
    # تحليل الفيديو باستخدام MediaPipe (مثال مبسط)
    cap = cv2.VideoCapture('temp.mp4')
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        # تحليل إحداثيات اليدين
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            # هنا تضيفون منطقكم لتحويل الإحداثيات إلى نص (مثال: حركة "مرحبًا")
            text = "مرحبًا"  # هذا نص وهمي - تحتاجون نموذجًا مدربًا للغة الإشارة العربية
    
    cap.release()
    return jsonify({"text": text})

if __name__ == '__main__':
    app.run(debug=True)
