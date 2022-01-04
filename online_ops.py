import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

def search_on_wikipedia(query):
    results = wikipedia.summary(query,sentences = 2)
    return results

def play_on_youtube(video):
    kit.playonyt(video)

