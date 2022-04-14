import speech_recognition as sr
import pyttsx3

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

            if 'vivi' in command:
                print(command)
        
    except:
        pass
    return command

def run_vi():
    command = take_command()
    if 'hey' in command:
        talk("Hi I'm Vivi. Welcome to the E-Academic Advisory system.")

while True:
    run_vi()