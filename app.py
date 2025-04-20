from flask import Flask, render_template, request, jsonify
import cv2
import mediapipe as mp
import os

app = Flask(__name__)

# تهيئة MediaPipe لتحليل اليدين
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'video' not in request.files:
        return jsonify({"error": "لم يتم رفع فيديو"}), 400
    
    video = request.files['video']
    video_path = "temp_video.mp4"
    video.save(video_path)
    
    # تحليل الفيديو
    detected_text = analyze_video(video_path)
    os.remove(video_path)  # حذف الفيديو بعد التحليل
    
    return jsonify({"text": detected_text})

def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # تحليل إحداثيات اليدين
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        
        if results.multi_hand_landmarks:
            # هنا يمكنك إضافة منطق الترجمة الفعلي
            return "مرحبًا"  # نص تجريبي
        
    cap.release()
    return "لم يتم التعرف على الإشارة"

if __name__ == '__main__':
    app.run(debug=True)
