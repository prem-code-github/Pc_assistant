import requests
import json
import pyttsx3
import time
engine = pyttsx3.init()
from win32com.client import Dispatch
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate",140)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def short_news():
    url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=3360b49084a44adebfba243bd2b73bfe'
    open_bbc_page=requests.get(url).json()
    article=open_bbc_page["articles"]
    result=[]
    for ar in article:
        result.append(ar["title"])

    for i in range(5):
        print(i+1,result[i])
        time.sleep(1.5)
        speak(result[i])
    speak('These were the top 5 headlines, Have a nice day  !!..')

def full_news():
    url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=3360b49084a44adebfba243bd2b73bfe'
    open_bbc_page=requests.get(url).json()
    article=open_bbc_page["articles"]
    result=[]
    for ar in article:
        result.append(ar["title"])

    for i in range(len(result)):
        print(i+1,result[i])
        time.sleep(1.5)
    
    speak(result)
    speak('These were the top headlines, Have a nice day  !!..')

if __name__ == '__main__':
    short_news()
    full_news()