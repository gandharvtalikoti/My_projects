import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio

import webbrowser
import pywhatkit as kit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)                    #0->is male voice and 1-> female voice

# set weather we want male or female voice
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)  # this speaks
    engine.runAndWait()


def Wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening")
    speak("I am Tom, Please tell me how may i help you?")


def takeCommand():
    # it takes microphoone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)  # from mic source..

    try:  # use try when u fell here error
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:  # when jarvis fails to listen u control comes in Exception
        print(e)
        print("Say that again Please....")
        return "None"
    return query


# def sendEmail(to, content):
#     server.ehlo()
#     server.starttls()
#     server.login('gandharvtalikoti12@gmail.com', 'your-password')
#     server.sendmail('gandharvtalikoti12@gmail.com', to, content)
#     server.close()

Wishme()
while True:
    query = takeCommand().lower()

    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak("Searching wikipedia.......")
        # replacing wikipedia in query with blank
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(f'According to wikipedia {results}')

    elif 'open youtube' in query:
        speak("opening youtube sir, here you go!")
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        speak("opening google sir, here you go!")
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        speak("opening  stackoverflow sir, here you go!")
        webbrowser.open("stackoverflow.com")

    elif 'open v3 school' in query:
        speak("opening  we3school sir, here you go!, keep learning new things!")
        webbrowser.open("we3school.com")

    # elif 'play music' in query:
    #     mus
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\gandh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"


    elif 'open netflix' in query:
        speak("opening netflix , here you go!, Enjoy watching netflix and chill")
        webbrowser.open("netflix.com")


    elif 'play attention by charlie puth' in query:
        speak("playing attention by charlie puth, on youtube here you go sir")
        kit.playonyt('attention by charlie puth')
        # webbrowser.open("https://www.youtube.com/watch?v=nfs8NYg7yQM")

    elif 'play drag me down by one direction' in query:
        speak("playing drag me down by one direction, on youtube here you go sir")
        webbrowser.open("https://www.youtube.com/watch?v=Jwgf3wmiA04")


    elif 'play all night by the vamps' in query:
        speak("playing all night by the vamps, on youtube here you go sir")
        webbrowser.open("https://youtu.be/xP26jmvNfWY")
    

    elif 'tom quit' in query:
        speak("Ok sir, you can call me anytime!")
        exit()

    elif 'you need a break' in query:
        speak("Ok sir, you can call me anytime!")
        speak("Just say hey Tom!")
        break

    

        




    # elif 'email to harry' in query:                       
    #     try:
    #         speak("What should I say?")
    #         content = takeCommand()
    #         to = "harryyourEmail@gmail.com"       
    #         sendEmail(to, content)
    #         speak("Email has been sent!")
    #     except Exception as e:
    #         print(e)
    #         speak("Sorry my friend harry bhai. I am not able to send this email")


    
