import clipboard
import datetime
import os
import psutil
import pyautogui
#import pyjokes
import pyttsx3
import pywhatkit
import requests
import smtplib
import speech_recognition as sr
import time as ti
import webbrowser as we
from email.message import EmailMessage
from newsapi import NewsApiClient
#from secrets import senderemail, password
from time import sleep


user = "V"
assistant = "Jarvis"

## this section manages the text to speech ability of Niyah ##

engine = pyttsx3.init()

# Set Niyahs speech rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-34)

# Sets Niyahs Voice
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    
    
    
    
engine.say('Hello mrs.Vigo, how can I help?')

engine.runAndWait()

