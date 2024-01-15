import pyttsx3
import os
import datetime
import time
import variables
import wolframalpha
import requests
import webbrowser
import random
import sys
import json
import speech_recognition as speech
from num2words import num2words
from win10toast import ToastNotifier
import winsound
import geocoder



cnewscheck = 0
question = ["what", "why", "how", "who", "where"]
opt=False
engine = pyttsx3.init("sapi5")  
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 130)

def speak(audio):
    engine.say(audio)  # Speak functions
    engine.runAndWait()

def wishme():
    a = random.choice(variables.greetings)
    speak(a)
    return a




def weather():
    apikey = variables.openweather
    g = geocoder.ip('me')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={g.city}&appid={apikey}&units=metric"
    weatherreq = requests.get(url)
    x = weatherreq.json()
    y = x["main"]
    t = y["temp"]
    p = y["pressure"]
    h = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    a = f"Temperature is {str(t)} degrees Celsius.\nThe atmospheric pressure is {str(p)} in HPA units.\nThe humidity is {str(h)} percent.\nThe weather can be described as {str(weather_description)}"
    speak(a)
    return a
# Correctly indented
def news():
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "55bb935bc77641058a8b245a2e33e239"
    }
    main_url = "https://newsapi.org/v1/articles"
    res = requests.get(main_url, params=query_params)
    result = res.json()
    article = result["articles"]
    results = []
    i = 0
    while i!=10:
        for ar in article:
            results.append(ar["title"])
            i+=1
    print(results)
    a = ""
    j = 1
    for arti in results:
        a += f"{j}) {arti}\n"
        j +=1
        speak(arti)
    return str(a)


def addordinal(n):
    ordinal = num2words(n, to="ordinal_num")  # ordinal values 1 too first
    return ordinal

def notes():
    try:
        with open('notes.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        with open('notes.json', 'w') as f:
            data = json.load(f)
    speak("What should the title of our note be? ")
    print("What should the title of our note be? ")
    y = takecommand()
    speak("What do you want me to note down? ")
    print("What should the title of our note be? ")
    z = takecommand()
    data[y] = z
    with open('notes.json', 'w') as f:
        json.dump(data, f)
    speak("Noted.")
    print("Noted.")

def reminder(title,message,duration):
    toaster=ToastNotifier()
    try:
        duration=duration.split()
        if(duration[0].isnumeric()):
            if(duration[1] in ["m","min","minutes","minute"]):
                timee=60*int(duration[0])
            elif(duration[1] in ["s","secs","seconds","sec","second"]):
                timee=int(duration[0])
            elif(duration[1] in ["h","hrs","hours","hour"]):
                timee=60*60*int(duration[0])
            time.sleep(timee)
            toaster.show_toast(title,message,duration=5)
            a = f"Your reminder with the title {title},message {message} is now triggered"
            speak(a)
            print(a)
            return a
    except Exception as e:
        print(e)
        a = "Wrong format of duration,Retry again!"
        speak(a)
        print(a)
        return a
    


def ai(query):

    if (query.startswith('jarvis')):
        query= query[6:]
        return wishme()
    if("open" in query):
        if query.endswith("notepad"):
            speak("opening Notepad..")
            print("opening Notepad..")
            notepad=variables.notepad
            os.startfile("C:\\Windows\\notepad.exe")
            return "Opening Notepad.."
        elif query.endswith("calculator"):
            speak("Opening Calculator..")
            print("Opening Calculator..")
            calculator=variables.calculator
            os.startfile(calculator)
            return "Opening Calculator.."
                
    if any(query.startswith(keyword) for keyword in question):
        if "weather" in query:
            return weather()
        elif query.endswith("time"):
            speak(f"The time right now is {(str(datetime.datetime.now())[11:16])}  ..")
            print(f"The time right now is {variables.time}  ..")
            return (str(datetime.datetime.now())[11:16])
        elif query.endswith("date today") or query.endswith("date"):
            speak(f"The date today is {variables.date}.")
            print(f"The date today is .")
            return variables.date
        else:
            try:
                client = wolframalpha.Client(variables.wolframalpha)
                res=client.query(query)
                print(next(res.results).text)
                answer = next(res.results).text
                speak(f"The Answer is {answer}")
                return answer
            except:
                speak("I'm sorry, I could not understand you. I will search the web for an answer. Hang on! ")
                print("I'm sorry, I could not understand you. I will search the web for an answer. Hang on! ")
                return "I'm sorry, I could not understand you. I will search the web for an answer. Hang on! "
                base_url = "http://www.google.com/search?q="
                final_url = base_url + query.replace(" ","%20")
                webbrowser.open(final_url, new = 2)
    if(("news") in query or "headlines" in query):
        return news()
        
        #return [b for b in news()]
    if (query.startswith("search") or query.startswith("google")):
        speak("Searching. Please wait!")
        print("Searching. Please wait!")
        base_url = "http://www.google.com/search?q="
        query = query[6:]
        final_url = base_url + query.replace(" ","%20")
        webbrowser.open(final_url, new = 2)
        return "Searching. Please wait!"        

    if(query.startswith("stop")):
        speak("Understood. ")
        speak("Shutting down now....")
        time.sleep(3)
        sys.exit()
                        
            
            
    if ("take a note" in query or "note down" in query or "add a note" in query or 'create note' in query):
        try:
            with open('notes.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            with open('notes.json', 'w') as f:
                a = {}
                json.dump(a,f)
            with open('notes.json','r') as f:
                data = json.load(f)
                speak("What should the title of our note be? ")
                print("What should the title of our note be? ")
                y = takecommand()
                speak("What do you want me to note down? ")
                print("What do you want me to note down? ")
                z = takecommand()
                data[y] = z
            with open('notes.json', 'w') as f:
                json.dump(data, f)
                speak("Noted.")
                print("Noted.")

    if ("show me my notes" in query or "list notes" in query):
        try:
            with open('notes.json', 'r') as f:
                data = json.load(f)

            keys = data.keys()
            i = 0
            for ke in keys:
                i +=1
            print("Searching for Notes....")
            speak("Searching for Notes....")
            print()
            return f"You have {num2words(i)} Notes..."
            speak(f"You have {num2words(i)} Notes...")
            print("Reading Note Headlines now..")
            speak("Reading Note Headlines now..")                         
             
            for keys in keys:
                speak(keys)
                print()
                return keys+": "+data[keys][:10]+"......"
        except FileNotFoundError:
            print("You have no notes. Would you like to create one?")
            speak("You have no notes. Would you like to create one?")
            b = takecommand().lower
            if ("yes" in b):
                notes()
            else:
                speak("Understood!")
        except Exception as e:
            speak("Unknown Error")
            print(e)
    if("set reminder" in query or "remind me" in query):
        speak("what do you want to add as the title")
        print("what do you want to add as the title")
        tl=takecommand()
        speak("What do you want the message to be:")
        print("What do you want the message to be:")
        mes=takecommand()
        speak("After what amount of time do you want to get notified about it?")
        print("After what amount of time do you want to get notified about it?")
        dur=takecommand()
        reminder(tl,mes,dur)


def speech_to_text():
    r=speech.Recognizer()
    with speech.Microphone() as source:   
        speak("Listening")
        r.pause_threshold=0.4
        r.non_speaking_duration=0.4
        r.energy_threshold=300
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio, language="en-in")
        except Exception as e:
            speak("Couldn't catch what you said")
            return " "
        return query

def takecommand():
    if(opt==True):
        speech_to_text()
    else:
        query=input("Input: ")
        try:
            print("Recognizing.....")
            print("User:", query)
        except Exception as e:
            return " "

        return query



