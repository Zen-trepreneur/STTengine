import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr
engine= pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    Time.datetime.datetime.now().strftime("%I:%M1:%S")
    
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)

    speak(date)
    speak(month)
    speak(year)
def takeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r .pause_threshold = 1
        
        audio = r.listen(source)
    try:
        print("Recongnizning. ..")
        query = r.recognize_google(audio,language='en-in' )
        print (query)
    
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    
    return query
    takeCommand()
    
if __name__=="__main__":
    while True:
    
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date( )
        elif 'offline' in query:
            quit()
    

