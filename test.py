import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("hello this is a very long sentence. and this is for me to perfectly use my vocabulary as i am a voice assistant! this is also used for decidinmg the rate of me speaking and the accent even though i cannot change it")
    engine.runAndWait()
    engine.stop()
