import speech_recognition as sr
import pyttsx3
import webbrowser as web
import wikipedia

listener = sr.Recognizer() #Recognizer Class helps to recognize speech
engine = pyttsx3.init()

#Get All Voices Available With Package
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source) #Speech Recognizer is listening to source    
            #Utilizes Google API to recognize Voice Activity from user
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa', '')
        
    except:
        pass
    return command

def run_vi():
    command = take_command()
    if 'hi' or 'hey' in command:
        talk("Hi I'm Alexa. Welcome to the E-Academic Advisory system. If you want to know more about me and how I work with the entire system. Say general overview")
    elif 'general overview' in command:
        talk("The E-Academic System is designed to assist Ashesi students with easy navigation of courses pertaining to their majors and current academic standings. It utilizes information from each student's data to tailor usage of the platform to students' best interests.")
    elif 'describe' in command:
        thing = command.replace('describe', '')
        
        description = wikipedia.summary(thing, 1)
        print(description)
        talk(description)
    elif 'electives' and 'Computer Science' in command:
        talk('Opening the Ashesi website to view electives')
        url = 'https://www.ashesi.edu.gh/academics/programmes/arts-and-sciences/liberal-arts-core-courses.html'
        web.open(url)
    else:
        talk('Kindly repeat your command.')

while True:
    run_vi()