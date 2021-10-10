# !pip install speechrecognition pyttsx3 googletrans

import speech_recognition as sr
import pyttsx3
from googletrans import Translator

r = sr.Recognizer()

"""### If you get an error "Microsoft Visual C++ 14.0 is required" or "PyAudio module not found" then follow the steps in README.txt"""

# Execute only if you get an error above
# !pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl


"""## Define your microphone"""

# Remove the following comment to see your input devices
# print(sr.Microphone.list_microphone_names())

mic = sr.Microphone()

"""## Recognize Speech"""

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    result = r.recognize_google(audio)

# If you want to see your result, execute the following
# print(result)

"""# Building the Translator
## Define Translator
"""

p = Translator()
k = p.translate(result, dest='spanish')
# you can put any language in the destination attribute, I have used spanish

# Here we convert the translated result into a text format
translated = str(k.text)
print(translated)

"""# Text to Speech Engine
## Define Text to Speech Engine
"""

engine = pyttsx3.init()

# Define the language of the translator
# Here is the code to see the list of languages and their IDs, which we will need when we are defining the translator.
# It is recommended to run this code before going to the next step.
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)

"""## Define the speaker language
### Copy the ID of the language that you want to use from the above code and paste it into your program.
"""

# Here I have used ID from my machine. Please use your ID in this code
fr_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', fr_voice_id)

# output the voice by the following
engine.say(translated)
engine.runAndWait()
