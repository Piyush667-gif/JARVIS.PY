import os
import smtplib
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
import pyttsx3
import datetime
import os 
import keyword, controller

import random
import pywhatkit as kit
import sys
import requests
import time
import operator

import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia

import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Alex Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='in-en')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search on youtube' in query:
             query = query.replace("search on youtube", "")
             webbrowser.open(f"www.youtube.com/results?search_query={query}")
             
        elif 'open youtube' in query:
            speak("what you will like to watch ?")
            qrry = takeCommand().lower()
            kit.playonyt(f"{qrry}")


        elif 'close youtube' in query:
            os.system("taskkill /f /im msedge.exe")    


        elif 'open google' in query:
            speak("what should I search ?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            speak(results)

        elif 'close google' in query:
            speak("i am closing google")
            os.system("taskkill /f /im msedge.exe")

        

        elif 'open stackoverflow' in query:
            speak("opening stackoverlow for you sir")
            webbrowser.open("stackoverflow.com")   
        
        elif'open telegram' in  query:
            speak("opening telegram for you sir, now you can chat or study ")
            tgcodepath="C:\\Users\pc\\AppData\\Roaming\\Telegram Desktop"
            os.startfile(tgcodepath)

        elif'open typing master' in query:
            speak('opening typing master for you sir')
            tmcodepath="C:\\Program\\Data\\Microsoft\\Start..."

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\pc\\Downloads\\RONALD1.py"
            speak("opening code for you sir")
            os.startfile(codePath)
        
        elif'open ninja' in query:
            webbrowser.open("www.codingninjas.com")
            speak("opening coding ninja sir! ypu can code now")

        elif'open leetcode' in query:
            webbrowser.open("leetcode.com") 
            speak("opening leet code")  
           

        elif 'email to piyush' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "piyushyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend piyush bhai. I am not able to send this email")    
            
        elif'shutdown'in query:
            speak("system get shutdown")
            os.system("shutdown /s /t 5")

        elif "restart pc" in query:
           speak("system get restart")
           os.system("shutdown /r /t 5")    

        elif("open notepad")  in query:
            speak("OK I AM opening notepad")
            npath="C:\\WINDOWS\\system32\\notepad.exe"

        elif "close notepad" in query:
           speak("OK I AM closing notepad")
           os.system("taskkill /f /im notepad.exe")
        
        elif "go to sleep" in query:
          speak(" alright then, I am switching off")
          sys.exit()
        
        elif "take screenshot" in query:
          speak('tell me a name for the file')
          name = takeCommand().lower()
          time.sleep(3)
          img = pyautogui.screenshot() 
          img.save(f"{name}.png") 
          speak("screenshot saved")

        elif "volume up" in query:
         speak("sir i increase the volume")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")
         pyautogui.press("volumeup")

        elif'volume down' in query:
         speak("sir i am decrease the volume")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")
         pyautogui.press("volumedown")   

        elif "silent" in query:
         speak("ok i am muting the system")
         pyautogui.press("volumemute")


        elif "refresh" in query:
         speak("ok i am refreshing the system")
         pyautogui.moveTo(1551,551, 2)
         pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
         pyautogui.moveTo(1620,667,1)
         pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')


        elif "scroll down" in query:
         speak("ok i will  scroll down ")
         pyautogui.scroll(1000)

        elif "rectangular spiral " in query:
         pyautogui.hotkey('win')
         time.sleep(1)
         pyautogui.write('paint')
         time.sleep(1)
         pyautogui.press('enter')
         pyautogui.moveTo(100, 193, 1)
         pyautogui.rightClick
         pyautogui.click()
         distance = 300
         while distance > 0:
           pyautogui.dragRel(distance, 0, 0.1, button="left")
           distance = distance - 10
           pyautogui.dragRel(0, distance, 0.1, button="left")
           pyautogui.dragRel(-distance, 0, 0.1, button="left")
           distance = distance - 10
           pyautogui.dragRel(0, -distance, 0.1, button="left")

        elif "close paint" in query:
           speak("ok sir i am closing the paint")
           os.system("taskkill /f /im mspaint.exe")

        elif 'maximize this window' in query:
           speak("piyush my friend i maximize the window")
           pyautogui.hotkey('alt', 'space')
           time.sleep(1)
           pyautogui.press('x')

        elif 'google search' in query:
           speak("i am searching piyush")
           query = query.replace("google search", "")
           pyautogui.hotkey('alt', 'd')
           pyautogui.write(f"{query}", 0.1)
           pyautogui.press('enter')

        elif 'youtube search' in query:
          speak("i am searching sir")
          query = query.replace("youtube search", "")
          pyautogui.hotkey('alt', 'd')
          time.sleep(1)
          pyautogui.press('tab')
          pyautogui.press('tab')
          pyautogui.press('tab')
          pyautogui.press('tab')
          time.sleep(1)
          pyautogui.write(f"{query}", 0.1)
          pyautogui.press('enter')


        elif 'open new window' in query:
          speak("ok boss i open the new window")
          pyautogui.hotkey('ctrl', 'n')  


        elif 'open incognito window' in query:
           speak("ok piyush iam opening incognito window")
           pyautogui.hotkey('ctrl', 'shift', 'n')


        elif 'minimise the window' in query:
          speak("ok piyush i minimise the window")
          pyautogui.hotkey('alt', 'space')
          time.sleep(1)
          pyautogui.press('n')  
        

        elif 'open history' in query:
          speak("ok piyush, i am opening history")
          pyautogui.hotkey('ctrl', 'h')


        elif 'open download' in query:
          speak("ok sir , i will open downloads")
          pyautogui.hotkey('ctrl', 'j')


        elif 'previous tab' in query:
          speak("ok i see you last tab")
          pyautogui.hotkey('ctrl', 'shift', 'tab')
          pyautogui.hotkey('ctrl', 'tab')

        elif 'close tab' in query:
          speak("ok sir , i am closing tab")
          pyautogui.hotkey('ctrl', 'w')

        elif 'close window' in query:
          speak("i am closing window")
          pyautogui.hotkey('ctrl', 'shift', 'w')

        elif 'clear browsing history' in query:
          speak("i a, clearing history")
          pyautogui.hotkey('ctrl', 'shift', 'delete')


        elif 'close chrome' in query:
          speak("i am closing chrome")
          os.system("taskkill /f /im chrome.exe")

     

    
         
        

