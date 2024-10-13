import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
from dateutil import relativedelta
import os
from time import sleep
import pywhatkit
import wikipedia
import pyautogui #jisse aap keyboard ka koi bhi key press kar skte h through python 
from hugchat import hugchat
    
def generate_text(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="./cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    return response  
    
def sptext():
    while True:
        recognizer=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            recognizer.adjust_for_ambient_noise(source)
            audio=recognizer.listen(source)
            try:
                print("Recogining....")
                data=recognizer.recognize_google(audio)
                print("You said -> ",data)
                return data
            except sr.UnknownValueError:
                print("Please say that again")
def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
def greeting():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speechtx("Good Moring, sir")
    elif hour>12 and hour<=18:
        speechtx("Good Afternoon, sir")
    else:
        speechtx("Good Evening sir")
def searchGoogle(data1):
    if "google" in data1:
        import wikipedia as googleScrap
        data1=data1.replace("jarvis","")
        data1=data1.replace("google search","")
        data1=data1.replace("google","")
        print
        speechtx("This is what I found on google")
        try:
            pywhatkit.search(data1)
            result=googleScrap.summary(data1,1)#1 means 1 line in wikipedia
            speechtx(result)
        except:
            speechtx("No speakable output available")
        
def searchYoutube(data1):
    if "youtube" in data1:
        speechtx("This is what I found for your search!")
        data1=data1.replace("jarvis","")
        data1=data1.replace("youtube search","")
        data1=data1.replace("youtube","")
        data1=data1.replace("search youtube","")
        data1=data1.replace("play songs","")
        web = "https://www.youtube.com/results?search_query="+data1 #open krke dede youtube
        webbrowser.open(web)
        pywhatkit.playonyt(data1) #Means jo first video hogi usse related vo open krke dede
        speechtx("Done, sir")
def searchWeikipedia(data1):
    if "wikipedia" in data1:
        speechtx("Searching from Wikipedia....")
        data1=data1.replace("wikipedia","")
        data1=data1.replace("search wikipedia","")
        data1=data1.replace("jarvis","")
        results = wikipedia.summary(data1,sentences=2)
        speechtx("According to Wikipedia")
        print(results)
        speechtx(results)

dictapp={"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}
     
def openappweb(data1):
    speechtx("Launching Sir")
    if ".com" in data1 or ".co.in" in data1 or ".org" in data1:
        data1=data1.replace("open","")
        data1=data1.replace("jarvis","")
        data1=data1.replace("launch","")
        data1=data1.replace(" ","")
        webbrowser.open(f"https://www.{data1}")
    else:
        key=list(dictapp.keys())
        for app in key:#agar mne install app me se bola hai toh 
            if app in data1:
                os.system(f"start{dictapp[app]}")

def closeappweb(data1):
    speechtx("Closing sir")
    if "one tab" in data1 or "1 tab" in data1:
        pyautogui.hotkey("ctrl","w")
    elif "two tab" in data1 or "2 tab" in data1:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speechtx("All tabs are closed ")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in data1:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")        

if __name__ =='__main__' :
    if "wake up" in sptext().lower():
        greeting()
        while True:
            # if True:
            data1=sptext().lower()
            if "exit the program" in data1:
                speechtx("Thankyou, you are exited")
                break
            elif "hello" in data1:
               speechtx("Hello sir, How are you?")
            elif "am fine" in data1 or "me too fine"in data1:
                speechtx("That's Great.")
            elif "how r u" in data1 or "how are you" in data1:
               speechtx("I am fine, what's about you? ")
            elif "Thank u" in data1 or "Thankyou" in data1 or "Thanku" in data1 or "thank" in data1:
               speechtx("Welcome sir")
            elif "old are you" in data1:
                birthdate=datetime.date(2005,9,4)
                todayage=(datetime.date.today()-birthdate)
                delta = relativedelta.relativedelta(datetime.date.today(), birthdate)
                print("Years -> ,",delta.years,"Months -> ,",delta.months,"Days -> ,",delta.days)
                print("My Age is -> ",todayage)
                speechtx(f"My age is  {todayage}")
            elif 'the time' in data1:
                time=datetime.datetime.now().strftime("%H:%M")
                speechtx(f"Sir, the time is {time}")
                
            elif "volume up" in data1 or "increase volume" in data1:
                from keyboard import volumeup
                speechtx("Turning volume up, sir")
                volumeup()
            elif "volume down" in data1 or "decrease volume" in data1:
                from keyboard import volumedown
                speechtx("Turning volume down, sir")
                volumedown()
            elif "open" in data1:
                openappweb(data1)
            elif "close" in data1:
                closeappweb(data1)
            
            elif "google" in data1:
                searchGoogle(data1)
            elif "youtube" in data1:
                searchYoutube(data1)
            elif "wikipedia" in data1:
                searchWeikipedia(data1)
            elif "jokes" in data1 or "joke" in data1:
                joke_1=pyjokes.get_joke(language="en",category="neutral")
                print(joke_1)
                speechtx(joke_1) 
            else:
                generated_text=generate_text(data1)
                print(generated_text)
                speechtx(generated_text)
            sleep(2)         
    else:
        print("Very Very Thankyou")