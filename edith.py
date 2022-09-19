import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyaudio
from playsound import playsound
import os
import pywhatkit as kit
import random
import numpy as np
import cv2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
print(voices[0].id)
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning gokul")

    elif hour>=12 and hour<18:
        speak("good afternoon gokul")

    else:
        speak("good evening  gokul")

    
def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...") 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(F"Boss said: {query}\n")

    except Exception as e:
        print(e)
        print("say agian...") 
        return "None"
    return query              

if __name__ == "__main__":
    wishme()
    speak("how can you help boss")
    while True:
        #speak("boss audio not clear")
        query = takecommand().lower()

        if "wikipedia" in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=7)
            speak("according to wikipedia")
            print(results)
            speak(results) 

        elif "name" in query:
            speak("my name is edith   verison 11.0")
            
        elif "hii" in query:
            wishme() 
            speak(" hii iam edith how can i help gokul")

        elif"youtube" in query:
            webbrowser.open("http://youtube.com")

        elif"google" in query:
            webbrowser.open("http://google.com") 

        elif"crome" in query:
            webbrowser.open("http://google.com") 

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%A %I:%M %p")
            speak(F"sir the time now{strTime}")
            print(strTime)
            railtime = datetime.datetime.now().strftime("%H %I:%M %p")
            print(F"sir raiway time is {railtime}")

        elif"whatsapp" in query:
            speak("done boss open your whatsapp account sir")
            webbrowser.open("http://web.whatsapp.com")

        elif "classroom" in query:
            speak("done boss open your last semester classroom sir ")
            webbrowser.open("https://classroom.google.com/u/1/h")

        elif"instagram" in query:
            speak("of course sir opening your instagram page")
            webbrowser.open("http://www.instagram.com")

        elif"facebook"  in query:
            webbrowser.open("http://www.facebook.com")

        elif"mail" in query:
            speak("done boss opening ypur mail id")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif "college" in query:
            speak("ok bosss") 
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")     

        elif"song" in query:
            cmd=("done boss play songs","yes sir iam play your favorate song ","yes boss ")
            now=random.choice(cmd)
            speak(now)
            choose=("file:///E:/songs/69.mp3","file:///E:/songs/4.mp3","file:///E:/songs/5.mp3","file:///E:/songs/6.mp3","file:///E:/songs/8.mp3" ,"file:///E:/songs/12.mp3",  
                      "file:///E:/songs/18.mp3","file:///E:/songs/29.mp3","file:///E:/songs/39.mp3","file:///E:/songs/51.mp3","file:///E:/songs/59.mp3","file:///E:/songs/3.mp3","file:///E:/songs/100.mp3")
            songs=random.choice(choose)
            playsound(songs)  

                 
        
        elif"music" in query:
            music_dir = 'E:\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[47]))

             
        elif"next" in query:
            playsound("file:///E:/songs/8.mp3")


        elif"videos" in query:
            commend=("yes sir your favorate video song","done gokul play video song","yes boss video song play now")
            now=random.choice(commend)
            speak(now)
            list=[
                  "https://www.youtube.com/watch?v=_c2cpeGPCmo",
                  "https://www.youtube.com/watch?v=GU1hmTA71Zg",
                  "https://www.youtube.com/watch?v=qP8e7lFdEho",
                  "https://www.youtube.com/watch?v=EmyUJW5o5f0",
                  "https://www.youtube.com/watch?v=pbGTuJiC7bI",
                  "https://www.youtube.com/watch?v=Bjx7Bo5jWwo"]
            rand=random.choice(list)
            webbrowser.open(rand) 

        elif "trending" in query:
            speak("done boss opening youtube trending page ")
            webbrowser.open("https://www.youtube.com/feed/trending")

        elif "rgb calculator" in query:
            speak ("done sir opening r g b calculator")
            webbrowser.open("https://www.w3schools.com/colors/colors_rgb.asp")

        elif " notes" in query:
            speak ("done boss opening kivy notes")
            webbrowser.open("https://github.com/attreyabhatt/kivyMD-Basics")

        elif "icons" in query:
            speak("done sir opening kivy icons")
            webbrowser.open("https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py")

        elif "camera" in query:
            speak("done sir opening camera")

            cap =cv2.VideoCapture(0)

            while True:
                ret, frame =cap.read()
                width = int(cap.get(3))
                height = int (cap.get(4))

                image= np.zeros(frame.shape, np.uint8)
                smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
                image[:height//2, :width//2] =smaller_frame
                image[height//2:, :width//2] =smaller_frame 
                image[:height//2, width//2:] =smaller_frame
                image[height//2:, width//2:] =smaller_frame
                cv2.imshow('frame',image)

                if cv2.waitKey(1) == ord("c"):
                    break 
                
            
            cap.release()
            cv2.destroyAllWindows()

        elif "you do" in query:
            action=("any details in wikipedia",
                    "open camera",
                    "open whatsapp",
                    "open instagram",
                    "open facebook",
                    "open mail",
                    "operting class room",
                    "playing songs",
                    "open youtube",
                    "playing video songs",
                    "playing trendig videos",
                    "open r g b calculator",
                    "open kivy notes ",
                    "open kivy icons",
                    "and excetra functions")
            print(action)        
            speak(action)
            






































            





