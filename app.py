from get_voice import get_voice
from flask import Flask, render_template, jsonify, request
from utils import transText, SpeakText, save_error, play_mp3, tts_fptAI
# from ParlAI.parlai.core.agents import create_agent_from_model_file
import os
from chat import get_response

app = Flask(__name__)

# def Model_init():
#   # import model from the model file can be pretrained or fine tuned

#   blender_agent = create_agent_from_model_file("zoo:blender/blender_90M/model")
#   return blender_agent
url = 'https://api.fpt.ai/hmi/tts/v5'
payload = ''
headers = {
    'api-key': 'OaGgkRmCMzOoZbnwgX70IDWo77t0g5SW',
    'speed': '',
    'voice': 'banmai'
}
@app.post("/welcome")
def voice_welcome():
    welcome = "Xin chào, tôi là trợ lý ảo của Câu lạc bộ Doanh nhân Sài Gòn, tôi có thẻ giúp gì cho bạn?"
    # SpeakText(welcome)
    audio = tts_fptAI(welcome)
    play_mp3(audio)
    os.remove(audio)
    return jsonify(welcome)

@app.get("/")
def index_get():
    return render_template("base.html")



# @app.post("/voice_predict")
# def voice_predict():
#     text_input = get_voice()
#     text_to_sys = transText(text_input.lower(), scr_input="user")
#     try:
#         resp, tag = get_response(text_to_sys)
#         if tag == 'unknown_response':
#             blender_agent.observe({'text': text_to_sys, 'episode_done': False})
#             response = blender_agent.act() # From bot
#             response = response['text']
#             message = {"answer": transText(response, scr_input="bot")}
#             SpeakText(transText(response, scr_input="bot"), lang_input='vi')
#         else:
#             print("rule base tag: ", tag)
#             message = {"answer": transText(resp, scr_input="bot")}
#             SpeakText(transText(resp, scr_input="bot"), lang_input='vi')
#     except:
#         save_error('Voice chat mode error', 'voice_chat')
#     return jsonify(message)

# @app.post("/predict")
# def predict():
#     text_input = request.get_json().get("message")
#     text_to_sys = transText(text_input.lower(), scr_input="user")
#     try:
#         resp, tag = get_response(text_to_sys)
#         if tag == 'unknown_response':
#             blender_agent.observe({'text': text_to_sys, 'episode_done': False})
#             response = blender_agent.act() # From bot
#             response = response['text']
#             message = {"answer": transText(response, scr_input="bot")}
#         else:
#             print("rule base tag: ", tag)
#             message = {"answer": transText(resp, scr_input="bot")}
#     except:
#         save_error('Chat basic mode error', 'chat_basic')
#     return jsonify(message)

if __name__ == "__main__":
    # blender_agent = Model_init()
    app.run(host='0.0.0.0', port=3000, debug=True)