from flask import Flask, request, render_template, jsonify
import os
import cv2
import mediapipe as mp
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    video = request.files['video']
    path = 'temp.mp4'
    video.save(path)

    # تحليل الفيديو باستخدام MediaPipe
    result_text = detect_hand_sign(path)

    return jsonify({'text': result_text})

def detect_hand_sign(video_path):
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(video_path)
    hand_detected = False
    frame_count = 0

    while cap.isOpened() and frame_count < 30:
        success, image = cap.read()
        if not success:
            break

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = hands.process(image)
        frame_count += 1

        if result.multi_hand_landmarks:
            hand_detected = True
            break

    cap.release()
    hands.close()

    if hand_detected:
        return "تم الكشف عن يد في الفيديو."
    else:
        return "لم يتم اكتشاف يد في الفيديو."

if __name__ == '__main__':
    app.run(debug=True)