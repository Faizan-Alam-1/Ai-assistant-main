# pip install SpeechRecognition
# pip install PyAudio==0.2.11
import speech_recognition as sr 
import speak

def Speech_To_Text(ask = False):
    if ask:
        speak.speak(ask)
    r =  sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source) # methord 
        voice_data = ''
    try:
        voice_data = r.recognize_google(audio)
        print(voice_data)
    except sr.UnknownValueError:
           return "sorry, i not get it"
    except sr.RequestError:
            return 'No internet connect please turn on you internet'
    except sr.WaitTimeoutError:
            speak("soryy sir sorry, i not get it")            
    return voice_data    

