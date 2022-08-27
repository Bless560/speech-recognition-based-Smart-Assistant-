import pyttsx3
import datetime
import os
import requests
import speech_recognition as sr
import playsound
from playsound import playsound
import msvcrt as m
import wikipedia
import smtplib
import webbrowser as wb
import psutil


def wait():
    m.getch()

engine = pyttsx3.init()

#to change the voice, ranging from 0 to 5
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

#to change voice speed
newVoiceRate = 190 #default speed is 200words per minute
engine.setProperty('rate', newVoiceRate)

AIname = "Marvel"
def speak(audio): 
    print(AIname + ': ' + audio)
    engine.say(audio)
    engine.runAndWait()

def now():
    Time = datetime.datetime.now().strftime('%I:%M:%p')
    speak("The current time is")
    speak(Time)

def date():
    today = datetime.datetime.now().strftime('The date of today is %d %m %Y')
    speak(today)

def welcome():
    #speak("Welcome back sir")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <12:
        speak ("Good Morning! Welcome back")
    elif hour >=12 and hour < 17:
        speak ("Good afternoon! Welcome back")
    elif hour >=18 and hour <=24:
        speak("Good evening! Welcome back")
    else:
        speak("You should be sleeping by now, anyways, Good morning")
    speak(AIname + " at Your service, How can I help You")
    print('')
    #speak("I'm Listening...")
    print('')

internetstatus=0
url = "https://www.google.com/"
timeout = 1.5
try:
	request = requests.get(url, timeout=timeout)
	internetstatus=1
except (requests.ConnectionError, requests.Timeout) as Exception:
	internetstatus=2

def command(): 
    if internetstatus==1:
        # print(' ')
        print('Listening . . .')
        # print(' ')
        c=sr.Recognizer()
        with sr.Microphone() as source:
            c.pause_threshold=1
            audio=c.listen(source)    
        try:
            
            query = c.recognize_google(audio,language='en-US')
            print('Boss: ' + query)
        except sr.UnknownValueError:
            print('Sorry, I did\'t get that. :( Try typing the command, (tips: type 10 instead of "ten") ')
            query = str(input('your favor is: '))
        return query
    if internetstatus==2:
        speak('Sorry! No internet! If your pc is connected to the internet, type: internet')
        speak('Or if your pc is not connected to the internet,')
        query = str(input('Try typing your command: '))
        return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('test51@email.com', 'test123')
    server.sendmail('text@gmail.com', to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)

    # battery = str(psutil.sensors_battery())
    # speak("Battery is at ")
    # speak(battery.percent)

if __name__ == "__main__":
    os.system('cls')
    speak('successfully switch to online mode')
    playsound('C:/Project/Jordan/assets/poweron.mp3')
    welcome() 
    while True:
        query=command().lower()
        if "hello" in query or "hi" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak(f'Hello my boss')
            speak(f'How can I help you now boss?')
        
        elif "time" in query:
            os.system('cls')
            print('Boss: ' + query)
            now()
            speak(f'what else would you like me to do, boss?')

        elif "date" in query:
            os.system('cls')
            print('Boss: ' + query)
            date()
            speak(f'what else would you like me to do, boss?')

        elif "today" in query:
            os.system('cls')
            print('Boss: ' + query)
            date()
            speak(f'what else would you like me to do, boss?')

        elif "day" in query:
            os.system('cls')
            print('Boss: ' + query)
            date()
            speak(f'what else would you like me to do, boss?')


        elif "how are you" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak(f'I am feeling good today. Thank you')
            speak(f'How can I help you now boss?')

        elif 'google' in query or 'search' in query: 
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search now boss?')
            search=command().lower()
            url=f'https://www.google.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Google for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'look up' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search now boss?')
            search=command().lower()
            url=f'https://www.google.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Web for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'facebook' in query:
            os.system('cls')
            print('Boss: ' + query)
            url=f'https://www.facebook.com/'
            wb.get().open(url)
            speak(f'This is facebook for you')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'twitter' in query:
            os.system('cls')
            print('Boss: ' + query)
            url=f'https://twitter.com/'
            wb.get().open(url)
            speak(f'This is twitter for you')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif "find on wikipedia" in query:
            speak("Searching...")
            query = query.replace("Wikipedia", "")
            result = wikipedia.summary(query, sentence = 2)
            speak(result)
            speak(f'what else you would like me to do, boss?')

        elif "send email" in query:
            try:
                speak("What should I say")
                content = command()
                to = "xyz@gmail.com"
                sendmail(to, content)
            except Exception as e:
                speak(e)
                speak("Unable to send message")
            speak('what else can I do fo you, boss?')
        
        #Play on youtube
        elif "find on youtube" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search on youtube now boss?')
            search=command().lower()
            url = f'https://youtube.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Youtube for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        
        elif 'What can you do' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('1: I can tell you the time and weather.')
            speak('2: I also can open browser or youtube.')
            speak('3: In addition, I can open some review tests for your grade.')
            speak('4: Besides, I can open a typing test with many languages supported')
            speak('5: I can open translator, google maps and google earth too!')
            speak('So, what would you like me to do now boss?')

        elif "abilities" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('1: I can tell you the time and weather.')
            speak('2: I also can open browser or youtube.')
            speak('3: In addition, I can open some review tests for your grade.')
            speak('4: Besides, I can open a typing test with many languages supported')
            speak('5: I can open translator, google maps and google earth too!')
            speak('So, what would you like me to do now boss?')

        elif "Functions" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('1: I can tell you the time and weather.')
            speak('2: I also can open browser or youtube.')
            speak('3: In addition, I can open some review tests for your grade.')
            speak('4: Besides, I can open a typing test with many languages supported')
            speak('5: I can open translator, google maps and google earth too!')
            speak('So, what would you like me to do now boss?')

        elif 'help' in query: 
            os.system('cls')
            print('Boss: ' + query)
            speak('This is the instruction')
            os.startfile('instruction.docx')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak('So, what would you like me to do now boss?')

        elif 'created you' in query or 'made you' in query or 'maker' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('Mr. Nji Bless created me. How can I help you now, boss?')

        elif 'notepad' in query: 
            os.system('cls')
            print('Boss: ' + query)
            speak('Opening notepad')
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\notepad.lnk')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak('So, what would you like me to do now boss?')

        elif 'song' in query: 
            speak('Hope you enjoy!')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            os.startfile('D:/Jordan/assets/1.mp3')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'music' in query:
            speak('Hope you enjoy!')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            os.startfile('D:/Jordan/assets/1.mp3')
            wait()
            speak(f'what else you would like me to do, boss?')

        # system checkup
        elif 'system check' in query:
            cpu()
            speak(f'what else you would like me to do, boss?')

        elif 'offline' in query:
            speak('Now going offline')
            os.startfile('main4.py')
            quit()
        
        elif "stop" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("Assistant is off. Goodbye boss")
            playsound('C:/Project/Jordan/assets/poweron.mp3')
            quit()
        
        elif "shutdown" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("Assistant is off. Goodbye boss")
            playsound('C:/Project/Jordan/assets/poweron.mp3')
            quit()
         
        elif "quit" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("Assistant is off. Goodbye boss")
            playsound('C:/Project/Jordan/assets/poweron.mp3')
            quit()

        elif "see you later" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("Ok sir. Goodbye boss")
            playsound('C:/Project/Jordan/assets/poweron.mp3')
            quit()
        #else: 
            #speak("Please repeat, It is either I didn't get you well  or the command is not yet available")
