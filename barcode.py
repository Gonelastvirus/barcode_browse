import eel
import requests
import winsound
import configparser
import tkinter 
from tkinter import messagebox
config = configparser.ConfigParser()                                     
config.read('config.ini')
url=config.get('App', 'url')
config['App']['url']
token=config.get('App', 'token')
config['App']['token']
eel.init("web")
@eel.expose
def request_to(number):
    try:
        payload = {'token':token, 'data': number}
        requests.get(url, params=payload)
        winsound.Beep(2000,95)
    except:
        # hide main window
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showerror("!WARNING", "Something error may be url problem check it!")
eel.start("index.html",size=(600,360))
