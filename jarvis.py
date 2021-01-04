import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    
    else:
        speak("Good Evening Sir!")

    speak("I am Jarvis at your service. How may I help you")


def takeCommand(): #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Please say that again...")
        return "None"
    return query 


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # f = open("F:\Internal\Secret.txt")
    # c = f.read()
    # server.login('mohitsaran6@gmail.com', c)
    server.login('mohitsaran6@gmail.com', '13158920')
    server.sendmail('mohitsaran6@gmail.com', to, content)
    server.close()

 
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()    #Logic for executing tasks based on query
        
        if 'hello' in query or 'hello jarvis' in query:
            speak(f"Hello Sir")

        elif 'what\'s up' in query or 'how are you' in query or 'how\'s you' in query:
            speak(f"I am fine and full of energy Sir")
        
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Accordifng to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\ASUS\\Downloads\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs)-1)]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Sure Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'you can rest now' in query or 'ok bye' in query:
            speak(f"Sure Sir, have a good day")

        elif 'email to mohit' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mohitsaran02@gmail.com"
                sendEmail(to, content)
                speak("The email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")

                