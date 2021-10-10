# !pip install speechrecognition pyttsx3 googletrans

import speech_recognition as sr
import pyttsx3
from googletrans import Translator


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    return query


"""
# Building the Translator
# Define Translator

"""
result = takeCommand().lower()
k = Translator().translate(result, dest='spanish')

# you can put any language in the destination attribute, I have used spanish
# Here we convert the translated result into a text format

translated = str(k.text)
print(translated)
speak(translated)
