import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import sys


"""
pip install speechRecognition
pip install pyttsx3
pip install wikipedia
pip install pipwin
pipwin install pyaudio
pip install -U autopep8
"""

# I was getting error so i install pyaudio
# error in that too so i googled it on the stackover flow.

"""
# Text to Speech Engine
# Define Text to Speech Engine

"""


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am olivia Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

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
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('whyiswhen@gmail.com', 'my password')
    server.sendmail('whyiswhen@gmail.com', to, content)
    server.close()


def exitcode():
    sys.exit()


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def sp(text):
    print(text)
    speak(text)


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        #  if 'olivia' in query:
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            sp(results)

        elif 'hello' in query:
            speak("hello")

        elif 'how are you' in query:
            speak("i am fine")

        elif 'what you can do' in query:
            sp("I am olivia. I can Wish you According to the time of the day. Open websites like Google ,Youtube ,flipkart ,Stackoverflow. Search websites like Google ,YouTube. Give the Introduction of someone according to wikipedia Play music. Stop listening. Tell the current time.")

        elif 'wish me' in query:
            wishMe()

        elif 'open' in query:
            print("opening.....")
            if 'youtube' in query:

                webbrowser.open("https://www.youtube.com/")

            elif 'google' in query:
                webbrowser.open("https://www.google.com/")

            elif 'stack overflow' in query:
                webbrowser.open("https://www.stackoverflow.com/")

            elif 'flipkart' in query:
                webbrowser.open("https://www.flipkart.com/")

        elif 'play music' in query:
            music_dir = 'D:\\non critical\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            sp(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to chirag' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "whyiswhen@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend chirag sir. I am not able to send this email")

        elif 'stop music' in query:
            os.close("C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini64.exe")

        elif 'search' in query:
            speak('Searching ...')
            query = query.replace("search ", "")
            query = query.replace(" on ", "")

            if 'youtube' in query:
                query = query.replace("youtube", "")
                webbrowser.open(
                    f"https://www.youtube.com/results?search_query={query}")

            elif 'google' in query:
                query = query.replace("google", "")
                webbrowser.open(
                    f"https://www.google.com/search?q={query}&sourceid=olivia")

        elif 'clear' in query:
            clearConsole()

        elif 'joke' in query:
            print("I can't remember any joke")

        elif 'kill me' in query:
            speak("I won't")
            print("I won't")
        elif 'exit' in query:
            sp("exiting........")
            exitcode()
