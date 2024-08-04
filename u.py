import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('harvard.wav') as source:
    # r.adjust_for_ambient_noise(source, duration=0.3)
    audio_text = r.listen(source)
    try:
        t = r.recognize_google(audio_text)
        print("Text:", t)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except Exception as e:
        print("An error occurred: {0}".format(e))
