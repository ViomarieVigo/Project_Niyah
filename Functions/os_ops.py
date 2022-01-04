import webbrowser
from webbrowser import *
import subprocess


def open_Vscode():
   subprocess.run(["/usr/bin/open", "-a", "Visual Studio Code"])
    
def open_Chrome():
    browser = webbrowser.get('Chrome')
    browser.open('https://www.google.com/')

def open_github():
    subprocess.run(["/usr/bin/open", "-a", "GitHub Desktop"])
    
def open_cmd():
    subprocess.run(["/usr/bin/open", "-a", "Terminal"])