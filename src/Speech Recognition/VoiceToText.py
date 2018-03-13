import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Listening')
    audio = r.listen(source)
    print("Speech-To-Text: " + r.recognize_google(audio))
