
from tkinter import*
from PIL import Image , ImageTk
import speech_recognition as sr
import Speech_To_Text
import speak
import Action
import threading

def Introduction():
    speak.speak("Hello, i'm you virtual Assistant , how I can help you ?")


def Gui():
    root = Tk()
    root.geometry("550x550")
    root.title("AI Assistant")
    root.resizable(False,False)
    root.config(bg="#6F8FAF")

    # Main Frame
    Main_frame = LabelFrame(root , padx=100 ,  pady=7 , borderwidth=3 ,  relief="raised")
    Main_frame.config(bg="#6F8FAF")
    Main_frame.grid(row = 0 ,  column= 1 ,  padx= 55 ,  pady =  60)


    # Text Lable 

    Text_lable = Label(Main_frame, text = "AI Assistant" , font=("comic Sans ms" ,  14 , "bold" ) , bg = "#356696")
    Text_lable.grid(row=0 ,  column=0 , padx=20 , pady= 10)


    # Image 
    Display_Image = ImageTk.PhotoImage(Image.open("image/assitant.png"))

    # Image Lable 

    Image_Lable = Label(Main_frame, image= Display_Image)
    Image_Lable.grid(row = 1 ,  column=0 , pady=20)


    def exit_window(data):
        if data in 'exit':
            root.destroy()

    def fun():
        data =  Speech_To_Text.Speech_To_Text()
        Action_Data = Action.Action(data)
        if Action_Data != None :
            speak.speak(Action_Data)  
        else :
            speak.speak("sorry, i not get it")

        exit_window(data)     
        
        
    #button 

    button =  Button(Main_frame ,  text="ASK" , bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command= fun)
    button.grid(row = 3 ,  column=0 , pady = 10)

    root.mainloop()



threading.Thread(target=Introduction).start()

threading.Thread(target=Gui).start()



