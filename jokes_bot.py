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
    json_data = json.loads(response.content.decode('iso-8859-1'))

    joke = json_data['content']
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
