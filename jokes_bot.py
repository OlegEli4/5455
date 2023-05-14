import requests
import os
import random
from gtts import gTTS
from playsound import playsound

def get_joke():
    url = 'http://rzhunemogu.ru/RandJSON.aspx?CType=1'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    import json
    json_data = json.loads(response.text.encode('utf8').decode())

    joke = json_data['Анекдот']
    return joke

def text_to_speech(joke):
    tts = gTTS(joke, lang='en')
    filename = 'joke.mp3'
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def update_joke():
    joke = get_joke()
    text_to_speech(joke)