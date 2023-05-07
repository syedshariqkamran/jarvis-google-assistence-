import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
import pywhatkit
from twilio.rest import Client

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
        
    
    elif hour>=12 and hour<18:
        speak("good after noon shariq is every things all right")
    else:
        speak("good evening")
        
    speak("i am jarvis . please tell  me how can oi help you")
def takeCommand():
    
    
    r= sr.Recognizer()
    with sr.Microphone() as source:
        
        print("listning.....")
        r.pause_threshold=1
        audio = r.listen(source,0,8)
        
    try:
        print("recognizing....")
        query =r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
        
        
    except:
        print("say that again please.")
        return "none"
    return query
        
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
            
        elif 'open google' in query:
            
            webbrowser.open("google.com")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open ai' in query:
            webbrowser.open("https://chat.openai.com/")
            
        elif 'open instagram' in query:
            webbrowser.open("instaram.com")
            
        elif 'how are you' in query:
            speak("i am fine what about you ")
        elif 'fine' in query:
            speak("good")
        elif 'stop' in query:
            speak("ok sir ,i am going to sleep")
            exit(1)
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")
        elif "sleep" in query:
            speak("ok sir ,i am going to sleep")
            exit(1)
        elif "temperature" in query:
            
            search = "temperature "
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")
            
        elif 'search' in query:
            import wikipedia as googleScrap
            query=query.replace("about "," ")
            query=query.replace("jarvice"," ")
            query=query.replace("google search"," ")
            query=query.replace("google"," ")
            query=query.replace("what do you now about "," ")
            
            speak("this is what i found on internet")
            pywhatkit.search(query)
            try:
                
                result=googleScrap.summary(query,3)
                speak(result)
        
            except:
                
                speak("sorry no data available on internet")

        elif "where are you" in query:
            speak("i am here sir there is issue in network")
            
        elif "your birthday" in query:
            speak("i am just a python program  .i do not have birthday,  i am created by programmers to help you")
            
        elif "ok" in query:
            speak("yes,  how can i help you")
            
        elif "wait" in query:
            speak("ok i am waiting for your question ")
            
        elif "you can do" in query:
            speak("i can just   try  to help you in finding  answer")
            
        elif "love" in query:
            speak("love is waste of time  don't ask it again")
            
            
        elif " " not in query:
            speak("sorry")
            break
        elif "stop " not in query:
            speak("sorry")
            break
        elif "sleep " not in query:
            speak("sorry")
            break
        elif "      " not in query:
            
            speak('searching result')
            query = query.replace("search","")
            results=webbrowser.open('https://www.google.com/search?q=' +query)
            print(results)
            speak(results)
        
        
        elif "who are you" in query:
            speak("i am just a python program ,  i am created by programmers to help you")
            
        elif "about you" in query:
            speak("i am just a python program ,  i designed to help you in finding solution of question i feel good by solving your question and doubts")
            
        
        
          

            
            

    
            
            
            
            

            
       
         
        
            
            

            
            
           
            
        
            
          
        
                   
    
    
    
