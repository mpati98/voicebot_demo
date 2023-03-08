# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from flask import Flask, render_template, jsonify, request
from utils import transText, save_error, tts_fptAI, play_mp3


app = Flask(__name__)
url = 'https://api.fpt.ai/hmi/tts/v5'
payload = ''
headers = {
    'api-key': 'OaGgkRmCMzOoZbnwgX70IDWo77t0g5SW',
    'speed': '',
    'voice': 'banmai'
}

@app.get("/")
def index_get():
    return render_template("index.html")

@app.post("/welcome")
def voice_welcome():
    welcome = "Xin chào, tôi là trợ lý ảo của Câu lạc bộ Doanh nhân Sài Gòn, tôi có thẻ giúp gì cho bạn?"
    # SpeakText(welcome)
    audio = tts_fptAI(welcome)
    play_mp3(audio)
    return jsonify(welcome)

# @app.post("/voice_predict")
# def voice_predict():
#     text_input = request.get_json().get("message")

#     return jsonify(text_input)


# @app.post("/predict")
# def predict():
#     text_input = request.get_json().get("message")
#     text_to_sys = transText(text_input, scr_input="user")

#     return jsonify(text_to_sys)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000, debug=True)
