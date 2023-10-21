import pyttsx3
import os
import datetime
import variables
import wolframalpha
import requests
import time
import webbrowser
import random
import sys
from GoogleNews import GoogleNews
from num2words import num2words

googlenews = GoogleNews()
cnewscheck = 0
question = ["what", "why", "how", "who", "where"]

engine = pyttsx3.init("sapi5")  
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 130)

def speak(audio):
    engine.say(audio)  # Speak functions
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(random.choice(variables.greetings))
    elif hour >= 12 and hour < 18:  
        
        speak(random.choice(variables.greetings))
    else:
        
        speak(random.choice(variables.greetings))

def takecommand():
    query=input("Enter the request to the Assistant: ")
    try:
        print("Recognizing.....")
        print("User said :", query)
    except Exception as e:
        return " "
    
    return query
def weather():
    speak("Which city's weather do you want to know?")
    city = takecommand().lower()
    speak(f"Fetching the weather details in {city}")
    apikey = variables.openweather
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric"
    weatherreq = requests.get(url)
    x = weatherreq.json()
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = x["weather"]

    weather_description = z[0]["description"]
    speak(
        " Temperature is "
        + str(current_temperature)
        + "degrees celsius."
        + "\n The atmospheric pressure is "
        + str(current_pressure)
        + " \n in HPA units."
        + " \n The humidity is "
        + str(current_humidiy)
        + "percent"
        + " \n The weather can be described as "
        + str(weather_description)
    )
def news():
    while True:
        speak("Which topic do you want to hear the news or headlines on?")

        newstopic = takecommand().lower()
        if newstopic == "stop":
            break
        if newstopic == " ":
            cnewscheck += 1
            if cnewscheck > 1:
                speak("Logging off from news")
                break
            else:
                continue
        else:
            cnewscheck = 0
            speak(f"Getting news on {newstopic}")
            googlenews.get_news(newstopic)
            googlenews.result()
            a = googlenews.gettext()
            lnews = len(a)
            tempvar1 = ""
            if lnews > 5:
                for i in range(1, 6):
                    tempvar1 = a[i]
                    speak(addordinal(i))
                    time.sleep(0.5)
                    speak(tempvar1)

            else:
                for i in range(1, lnews + 1):
                    tempvar1 = a[i]
                    speak(addordinal(i))
                    time.sleep(0.5)
                    speak(tempvar1)

            googlenews.clear()

def addordinal(n):
    ordinal = num2words(n, to="ordinal_num")  # ordinal values 1 too first
    return ordinal

if __name__ == "__main__":
    while True:
        query=takecommand().lower()
        if(query.startswith('jarvis')):
            wishme()
            query= query[6:]
        if("open" in query):
            if query.endswith("notepad"):
                speak("opening Notepad..")
                notepad=variables.notepad
                os.startfile(notepad)
                query=""
            elif(query.endswith("calculator")):
                speak("Opening Calculator..")
                calculator=variables.calculator
                os.startfile(calculator)
            
        if any(keyword in query for keyword in question):
            if "weather" in query:
                weather()
            elif query.endswith("time"):
                speak(f"The time right now is {variables.time}  ..")
                print(variables.time)
            elif query.endswith("date today") or query.endswith("date"):
                speak(f"The date today is {variables.date}.")
  
            else:
                        try:
                            client = wolframalpha.Client(variables.wolframalpha)
                            res=client.query(query)
                            print(next(res.results).text)
                            answer = next(res.results).text
                            speak(f"The Answer is {answer}")
                        except:
                            speak("I'm sorry, I could not understand you. I will search the web for an answer. Hang on! ")
                            base_url = "http://www.google.com/search?q="
                            final_url = base_url + query.replace(" ","%20")
                            webbrowser.open(final_url, new = 2)
        if(("news") in query or "headlines" in query):
            news()  
        if (query.startswith("search") or query.startswith("google")):
            speak("Searching. Please wait!")
            base_url = "http://www.google.com/search?q="
            query = query[6:]
            final_url = base_url + query.replace(" ","%20")
            webbrowser.open(final_url, new = 2)        

        if("stop" in query):
            speak("Understood. Do you want me to shutdown or just keep quiet? ")
            y = takecommand().lower()
            if "shut down" in y:
                speak("Shutting down now....")
                time.sleep(3)
                sys.exit()
            elif "sleep" in y:
                break
            else:
                speak("I don't know what you mean..")
