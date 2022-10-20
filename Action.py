import datetime
import webbrowser
import Speech_To_Text
import os
import speak
import time

def Action(voice_data):
    if "what's your name" in  voice_data:
         return "my name is virtual Assistant"

    elif "hello" in voice_data or "hye" in voice_data or "hay" in voice_data:
        return "hello, i'm your virtual assistant"     

    elif "what's time now"  in voice_data:
           current_time = datetime.datetime.now()
           Time = (str)(current_time.hour)+" Hour", (str)(current_time.minute)+" Minute" 
           return Time

    elif "Facebook" in voice_data:
        webbrowser.open("https://www.facebook.com/")
        return "please wait facebook opening"   

    elif "email" in  voice_data or "Gmail" in  voice_data:
        webbrowser.open("https://mail.google.com/")
        return "please wait Gmail opening"

    elif "WhatsApp" in voice_data or "whatsapp" in voice_data:
        webbrowser.open("https://web.whatsapp.com/")  
        return "please wait Whatsapps opening"     

    elif 'search'  in voice_data:
        search = Speech_To_Text.Speech_To_Text('what you want to search for')  
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        return 'What i found for you '+ search + " in google"

    elif 'YouTube' in voice_data:
        search = Speech_To_Text.Speech_To_Text('what you want to search for')  
        url = 'https://youtube.com/search?q=' + search 
        webbrowser.get().open(url)
        return 'What i found for you ' + search + " in YouTube"

    elif 'play some music' in voice_data:
        url = 'D:\\music'   # Enter you music location 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        return "songs playing..."

    elif 'exit' in voice_data:
        speak.speak("Exit Done..")
        exit()  

