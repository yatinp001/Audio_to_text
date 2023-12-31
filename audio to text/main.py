import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile('Customer.wav') as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)
    print(text)
except sr.UnknownValueError:
    print("Could not understand audio")