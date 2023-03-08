import requests
import os
from gtts import gTTS
from playsound import playsound
import time
import wget
import subprocess

# src tu bot - vi tu user - en
def transText(text_input, scr_input='bot'):
    from googletrans import Translator
    # define a translate object
    translate = Translator()
    # Translate some text
    # scr_input = translate.detect(text_input)
    if scr_input == "bot":
        result = translate.translate(text_input, src='en', dest='vi')
        result = result.text
    elif scr_input == "user":
        result = translate.translate(text_input, src='vi', dest='en')
        result = result.text
    else:
        result = "We not support this language, please use English or Vietnamese!"
    return result

# Write error to txt


def save_error(message, error_source):
    f = open("error_log.txt", "a")
    # writing in the file
    f.write(error_source)
    f.write(str(message))
    f.write('\n')
    # closing the file
    f.close()

def SpeakText(command, lang_input='vi'):
    import os
    from gtts import gTTS
    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=command, lang=lang_input, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("temp.mp3")

    # Playing the converted file
    os.system("mpg123 temp.mp3")


def train_rb_model():
    pass

def tts_fptAI(msg):
    while True:
        try:
            url = 'https://api.fpt.ai/hmi/tts/v5'
            headers = {
                'api-key': 'OaGgkRmCMzOoZbnwgX70IDWo77t0g5SW',
                'speed': '',
                'voice': 'banmai'
            }

            response = requests.request('POST', url, data=msg.encode('utf-8'), headers=headers)
            response = response.json()
            file = response['async']
        except:
            time.sleep(1)
            continue
        break
    while True:
        try:
            wget.download(file)
        except:
            time.sleep(0.1)
            # print('Co loi. Thu lai', end='')
            continue
        break
    # print(resp)
    file_name = file.split('/')[-1]
    # playsound(file_name)
    return file_name

def play_mp3(path):
    subprocess.Popen(['mpg123', '-q', path]).wait()