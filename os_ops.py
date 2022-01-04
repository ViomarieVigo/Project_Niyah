import os
import subprocess

paths = {
    'VsCode': "/Applications/Visual Studio Code.app",
    'Chrome': "/Applications/Google Chrome.app",
    'terminal': "/System/Applications/Utilities/Terminal.app",
    'Github':"/Applications/GitHub Desktop.app"
}

def open_Vscode():
    os.startfile(paths['VsCode'])
    
def open_Chrome():
    os.startfile(paths['Chrome'])

def open_github():
    os.startfile(paths['Github'])
    
def open_cmd():
    os.startfile(paths['terminal'])