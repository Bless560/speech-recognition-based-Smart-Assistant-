from vosk import Model, KaldiRecognizer
import pyttsx3
import datetime
import pyaudio
import json
import os
import time
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
#speak("Hello, My name is " + AIname)

#Creating Time function
def now():
    Time = datetime.datetime.now().strftime('%I:%M:%p')
    speak("The current time is")
    speak(Time)

def date():
    today = datetime.datetime.now().strftime('The date of today is %d %m %Y')
    speak(today)

#Greeting Function
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
        speak("You should be sleeping by now, anyways Good morning")
    speak(AIname + " at Your service, How can I help You")
    print('')
    #speak("I'm Listening...")
    print('')

#playsound("C:/Users/Sivastien/Desktop/1.mp3")
model = Model("D:/Smart/Jordan/assets/vosk-model-small-en-us-0.15")
os.system('cls')
playsound('D:/Smart/Jordan/assets/poweron.mp3')
welcome()

rec = KaldiRecognizer(model, 16000)
cap = pyaudio.PyAudio()
stream =cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('test51@email.com', 'test123')
    server.sendmail('text@gmail.com', to, content)
    server.close()

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

            elif "time" in query or "clock" in query:
                os.system('cls')
                stream.stop_stream()
                print("Boss: " + query)
                now()
                speak("What else would you like me to do for you?")
                stream.start_stream()
                print('')
                #speak("I'm listening...")
                print('')
            
            elif "date" in query or "day" in query or "today" in query:
                os.system('cls')
                stream.stop_stream()
                print("Boss: " + query)
                date()
                speak("What else would you like me to do for you?")
                stream.start_stream()
                print('')
                #speak("I'm listening...")
                print('')

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
            elif "maps" in query:
                os.system('cls')
                print('Boss: ' + query)
                url = f'https://www.google.com/maps/'
                wb.get().open(url)
                speak(f'This is google maps')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif "glob" in query: #all global or globe returns to this code
                os.system('cls')
                print('Boss: ' + query)
                url = f'https://earth.google.com/web/@16.24291914,105.7762962,-1110.77003945a,12946843.60659599d,35y,0h,0t,0r'
                wb.get().open(url)
                speak(f'This is google earth')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif "earth" in query:
                os.system('cls')
                print('Boss: ' + query)
                url = f'https://earth.google.com/web/@16.24291914,105.7762962,-1110.77003945a,12946843.60659599d,35y,0h,0t,0r'
                wb.get().open(url)
                speak(f'This is google earth')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')

            elif 'translat' in query: 
                os.system('cls')
                print('Boss: ' + query)
                url=f'https://www.dict.cc/'
                wb.get().open(url)
                speak(f'This is german-english dictionary.')
                url2=f'https://jdict.net/'
                speak('...')
                speak('...')
                wb.get().open(url2)
                speak('this is Japanese-Vietnamese dictionary.')
                speak('...')
                url3=f'https://translate.google.com/'
                speak('...')
                wb.get().open(url3)
                speak('this is google translate.')
                url4=f'https://www.oxfordlearnersdictionaries.com/'
                speak('...')
                speak('...')
                wb.get().open(url4)
                speak(' and this is Oxford dictionary')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'dictionar' in query: 
                os.system('cls')
                print('Boss: ' + query)
                url=f'https://www.dict.cc/'
                wb.get().open(url)
                speak(f'This is german-english dictionary.')
                url2=f'https://jdict.net/'
                speak('...')
                speak('...')
                wb.get().open(url2)
                speak('this is Japanese-Vietnamese dictionary.')
                url3=f'https://translate.google.com/'
                speak('...')
                speak('...')
                wb.get().open(url3)
                speak('this is google translate.')
                url4=f'https://www.oxfordlearnersdictionaries.com/'
                speak('...')
                speak('...')
                wb.get().open(url4)
                speak(' and this is Oxford dictionary')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            
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


            elif 'weather' in query: 
                os.system('cls')
                print('Boss: ' + query)
                url=f'https://www.google.com/search?q=weather'
                wb.get().open(url)
                speak(f'This is your local weather!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'whether' in query: 
                os.system('cls')
                print('Boss: ' + query)
                url=f'https://www.google.com/search?q=weather'
                wb.get().open(url)
                speak(f'This is your local weather!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'climate' in query: 
                os.system('cls')
                print('Boss: ' + query)
                url=f'https://www.google.com/search?q=weather'
                wb.get().open(url)
                speak(f'This is your local weather!')
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
            elif 'browser' in query:
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
                playsound('D:/Smart/Jordan/assets/poweron.mp3')
                quit()
            elif "logout" in query:
                os.system('cls')
                os.system('shutdown -l')
                print('Boss: ' + query)
                speak("Assistant is off. Goodbye boss")
                playsound('D:/Smart/Jordan/assets/poweron.mp3')
                quit()
            
            elif "see you later" in query:
                os.system('cls')
                print('Boss: ' + query)
                speak("Ok sir. Goodbye boss")
                playsound('D:/Smart/Jordan/assets/poweron.mp3')
                quit()

            elif "see you" in query:
                os.system('cls')
                print('Boss: ' + query)
                speak("ok Later!. Goodbye boss")
                playsound('D:/Smart/Jordan/assets/poweron.mp3')
                quit()

            elif 'What can you do' in query or 'ability' in query or 'function' in query:
                os.system('cls')
                print('Boss: ' + query)
                speak('1: I can tell you the time and weather.')
                speak('2: I also can open browser or youtube.')
                speak('3: In addition, I can open some review tests for your grade.')
                speak('4: Besides, I can open a typing test with many languages supported')
                speak('5: I can open translator, google maps and google earth too!')
                speak('So, what would you like me to do now boss?')

            elif 'created you' in query or 'made you' in query or 'maker' in query:
                os.system('cls')
                print('Boss: ' + query)
                speak('Mr. Nji Bless created me. How can I help you now, boss?')
           
            elif 'song' in query: 
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('D:/Smart/Jordan/assets/1.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')

            elif 'music' in query:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('D:/Smart/Jordan/assets/1.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')

            elif 'online' in query:
                speak('Going online now and using speeach recognition')
                os.startfile('main.py')
                quit()

            elif 'open' in query:
                speak('Going online now and using speeach recognition')
                os.startfile('main4.py')
                quit()

            else: 
                speak("Please repeat, It is either I didn't get you well  or the command is not yet available")


if __name__ == '__main__':
    takecommand()


