import pyttsx3
from decouple import config

from datetime import datetime

import speech_recognition as sr
from random import choice

from utils import opening_text


USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init()

engine.setProperty('rate',150)

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[10].id)

# Text to speech 

def speak(text):
    engine.say(text)

# Greeting 
def greet_user():
    
    hour = datetime.now().hour
    if (hour >= 6 ) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour< 16):
        speak(f"Good Afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am{BOTNAME}. How may I assists you?")
    
# Speech recogniztion to text
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query

# 
    
engine.runAndWait()