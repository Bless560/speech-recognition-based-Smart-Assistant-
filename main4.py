from vosk import Model, KaldiRecognizer
import pyttsx3
import datetime
import pyaudio
import json
import os
import requests
import speech_recognition as sr
import playsound
from playsound import playsound
import msvcrt as m
import wikipedia
import smtplib
import webbrowser as wb

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
        print(' ')
        print('Listening . . .')
        print(' ')
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
        speak('Sorry! No internet! If your pc have connected to the internet, type: internet')
        speak('Or if your pc have not connected to the internet,')
        query = str(input('Try typing your command: '))
        return query


#Creating Time and date function
def now():
    Time = datetime.datetime.now().strftime('%I:%M:%p')
    speak("The current time is")
    speak(Time)

def date():
    today = datetime.datetime.now().strftime('The date of today is %d %m %Y')
    speak(today)

#Greeting Function
def welcome():
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <12:
        speak ("Good Morning! Welcome back")
    elif hour >=12 and hour < 17:
        speak ("Good afternoon! Welcome back")
    elif hour >=18 and hour <=24:
        speak("Good evening! Welcome back")
    else:
        speak("You should be sleeping by now, anyways Good morning")
    speak(AIname + " at Your service, How can I help You")
    speak("You are curretly using offline mode, to access online usage, please switch to online mode")
    print('')
    #speak("I'm Listening...")
    print('')
    
model = Model("assets/vosk-model-small-en-us-0.15")
os.system('cls')
playsound('C:/Project/Jordan/assets/poweron.mp3')
welcome()

rec = KaldiRecognizer(model, 16000)
cap = pyaudio.PyAudio()
stream =cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def takecommand():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            result = json.loads(result)
            query = result['text']
            print("Boss: " + query)
            
            if "map" in query:
                os.system('cls')
                print('Boss: ' + query)
                url = f'https://www.google.com/maps/'
                wb.get().open(url)
                speak(f'This is google maps')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')

            elif "time" in query:
                os.system('cls')
                print('Boss: ' + query)
                now()
                speak(f'what else you would like me to do, boss?')
            
            elif "date" in query:
                os.system('cls')
                print('Boss: ' + query)
                date()
                speak(f'what else you would like me to do, boss?')

            elif "today" in query:
                os.system('cls')
                print('Boss: ' + query)
                date()
                speak(f'what else you would like me to do, boss?')

            elif "day" in query:
                os.system('cls')
                print('Boss: ' + query)
                date()
                speak(f'what else you would like me to do, boss?')


            elif "hello" in query:
                os.system('cls')
                print('Boss: ' + query)
                speak(f'Hello my boss')
                speak(f'How can I help you now boss?')

            elif "how are you" in query:
                os.system('cls')
                print('Boss: ' + query)
                speak(f'I am feeling good today. Thank you')
                speak(f'How can I help you now boss?')
            
            elif 'google' in query: 
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

                #Search
            elif 'search' in query:
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

            #opening files
            elif 'notepad' in query: 
                os.system('cls')
                print('Boss: ' + query)
                speak('Opening notepad')
                os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\notepad.lnk')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak('So, what would you like me to do now boss?')


            #play on youtube
            elif "play" in query:
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
            
            elif "quit" in query:
                os.system('cls')
                print('Boss: ' + query)
                speak("Assistant is off. Goodbye boss")
                playsound('D:/Smart/Jordan/assets/poweron.mp3')
                quit()

            elif "stop" in query:
                os.system('cls')
                print('Boss: ' + query)
                speak("Assistant is off. Goodbye boss")
                playsound('C:/Project/Jordan/assets/poweron.mp3')
                quit()

            elif "see you" in query:
                os.system('cls')
                print('Boss: ' + query)
                speak("ok Later!. Goodbye boss")
                playsound('C:/Project/Jordan/assets/poweron.mp3')
                quit()

            elif 'function' in query:
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

            elif 'maker' in query:
                os.system('cls')
                print('Boss: ' + query)
                speak('Mr. Nji Bless created me. How can I help you now, boss?')
           
            elif 'song' in query: 
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('C:/Project/Jordan/assets/1.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')

            elif 'music' in query:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('C:/Project/Jordan/assets/1.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')

            elif 'online' in query:
                speak('Awitching to online mode.')
                os.startfile('online.py')
                quit()

            elif 'open' in query:
                os.startfile('main4.py')
                quit()

            else: 
                speak("Please repeat, It is either I didn't get you well  or the command is not yet available")


if __name__ == '__main__':
    takecommand()


