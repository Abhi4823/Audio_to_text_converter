import time
import speech_recognition as sr
from datetime import datetime

r = sr.Recognizer()
r.energy_threshold=300

def existingAudio(sr,r):
    with sr.AudioFile('intro.wav') as source:
       print("enter the audio")
       r.adjust_for_ambient_noise(source,duration=0.3)
       audio_text=r.listen(source)
       try:
           t=r.recognize_google(audio_text)
           print( "Text : " , t)
       except :
           print("Sorry, I am not able")


def viaMicrophone(sr, r):
    with sr.Microphone() as source:
        lang = input("Enter the language=").lower()
        print("Audio conversion now:")
        start_time = time.time()  # Record the start time
        while time.time() - start_time < 5:  # Continue loop until 5 seconds have passed
            # DSP: Adjust for ambient noise to improve speech recognition accuracy
            r.adjust_for_ambient_noise(source,duration=0.5)
            audio = r.listen(source)
            try:
                dict = {'english': 'en-IN', 'hindi': 'hi-IN', 'spanish': 'es-ES','japanese':'ja-JP','tamil':'ta-IN'}
                # DSP: Perform speech recognition on the captured audio
                text = r.recognize_google(audio, language=dict[lang])

                n = datetime.now()            
                print("recorded: {}".format(text))
                time.sleep(.5)
                if text == "stop recording":
                    print("Ending recording session")
                    break
            except sr.UnknownValueError:
                print("Google speech recognition could not understand your audio")
            except sr.RequestError as e:
                print("Could not request results from Google")
# existingAudio(sr,r)
viaMicrophone(sr,r)