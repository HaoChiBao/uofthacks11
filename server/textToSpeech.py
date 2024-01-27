from gtts import gTTS
import os
import speech_recognition as sr

while True:
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print('Say something...')
            audio = recognizer.listen(source)

        words = recognizer.recognize_google(audio)
        print(f"Recognized: {words}")

        intro_text = "Hello, my name is Furby and you’re going to be my best friend!"
        alarm_text = "AAAAAAAAAAAAAAAAAAAAAAAAAA"
        happy_text = "Yippeeeee! I can see that big smile on your face! Your happiness is contagious."
        mad_text = "You look mad. Why don’t you shake it off"
        sad_text = "Cheer up best friend! Turn that frown upside down!"

        def text_to_speech(my_text, language='en'):
            output = gTTS(text=my_text, lang=language, slow=False)
            output.save("output.mp3")
            os.system("afplay output.mp3")  # Use "afplay" for macOS

        if 'Furby' in words:
            if 'hello' in words:
                #print('Hello to you too!')
                text_to_speech(intro_text)
            elif 'alarm' in words:
                text_to_speech(alarm_text)

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")




'''
from gtts import gTTS
import os

import speech_recognition
import pyaudio
while True:
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('say something')
        audio = recognizer.listen(source)

    words = recognizer.recognize_google(audio)

    intro_text = "Hello, my name is Furby and you’re going to be my best friend!"
    happy_text = "Yippeeeee! I can see that big smile on your face! Your happiness is contagious."
    mad_text = "You look mad. Why don’t you shake it off"
    sad_text = "Cheer up best friend! Turn that frown upside down!"
    alarm_text = "AAAAAAAAAAAAAAAAAAAAAAAAAA"

    def text_to_speech(my_text, language='fr'):
        output = gTTS(text=my_text, lang=language, slow=False)
        output.save("output.mp3")

    print(words)

    if 'Furby' in words:

        if 'hello' in words:
            print('hello to you too!')
            text_to_speech(intro_text)
            os.system("afplay output.mp3")

        if 'alarm' in words:
            text_to_speech(alarm_text)
            os.system("afplay output.mp3")

'''







# language = 'en'
# language = 'fr'

#output = gTTS(text=my_text, lang=language, slow=False)

#output.save("output.mp3")

#os.system("afplay output.mp3") #command for mac, start for windows

