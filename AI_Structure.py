import pyttsx3
import os
import datetime
import random
import variables
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
    query=input("Enter the request to the Assistant:")
    try:
        print("Recognizing.....")
        print("User said :", query)
    except Exception as e:
        return " "
    
    return query

if __name__ == "__main__":
    while True:
        query=takecommand().lower()
        if(query.startswith('jarvis')):
            wishme()
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
        if (query.startswith("what")):
            if query.endswith("time"):
                speak(f"The time right now is {variables.time}  ..")
                print(variables.time)
            elif query.endswith("date today") or query.endswith("date"):
                speak(f"The date today is {variables.date}.")
