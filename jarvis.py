import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty("voice",voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning.")
    elif hour>=12 and hour<18:
        speak("Good Afternoon.")
    else:
        speak("Good Evening.")
    speak("I am JARVIS sir. How may i help you.")
def takeCommand():
    #It takes micro-phone input from the user and returns a string output.
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising.....")
        query=r.recognize_google(audio,language="en-in")
        print(f"User Said: {query}.")
    except Exception as e:
        #print(e)
        print("Sorry can't recognige. Please say that again.")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("youremail","password")
    server.sendmail("sender email",to,content)
    server.close()
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if "wikipedia" in query:
            speak=("Searching Wikipedia.....")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("According To Wikipedia.")
            prine(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir="Music"
            songs=os.listdir(music_dir)
            print(songs)
            os.start(os.path.join(music_dir,songs[0]))
        elif "play online music" in query:
            webbrowser.open("gaana.com")
        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}.")
        elif "open code" in query:
            codePath=r"Address where your code editor is installed"
            os.startfile(codePath)
        elif "who are you" in query:
            speak("I am JARVIS. Initially i was used in avengers seris.")
        elif "email to" in query:
            try:
                speak(r"What's the email.")
                content=takeCommand()
                to="Email"
                sendEmail(to,content)
                speak("E-mail has been sent.")
            except Exception as e:
                print(e)
                speak("The E-Mail has not been sent due to an ERROR.")
        elif "quit" in query or "exit" in query:
            speak("Quiting sir, Thank's for use.")
            exit()