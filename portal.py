import speech_recognition as sr
import pyttsx3
import webbrowser as web
import wikipedia
from flask import Flask, render_template, url_for, request

app = Flask(__name__)
@app.route('/')

def main():
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

                if 'ash' in command:
                    command = command.replace('ash', '')
            
        except:
            pass
        return command

    def run_vi():
        talk("Welcome to Ash Digital Assistant. Acces my functionalities by saying any of the below commands.")
        command = take_command()
        # if command == 'hi' or 'hey':
        #     talk("Hi I'm Ash. Welcome to the E-Academic Advisory system. If you want to know more about me and how I work with the entire system. Say description")
        if command == 'description':
            talk("The E-Academic System is designed to assist Ashesi students with easy navigation of courses pertaining to their majors and current academic standings. It utilizes information from each student's data to tailor usage of the platform to students' best interests.")
        elif 'hello' in command:
            talk("Hi I'm Ash. Welcome to the E-Academic Advisory system. If you want to know more about me and how I work with the entire system. Say description")
        elif command == 'view':
            talk('Opening the Ashesi website to view electives')
            url = 'https://www.ashesi.edu.gh/academics/programmes/computer-science/curriculum.html'
            web.open_new_tab(url)
        elif 'describe' or 'explain' or 'what is' in command:
            thing = command.replace('describe', '')   
            description = wikipedia.summary(thing, 1)
            print(description)
            talk(description)
        else:
            talk('Kindly repeat your command.')

        return "Ash is listening..."

    while True:
        run_vi()
    

if __name__ == "__main__":
    app.run(host="http://localhost/Ash/Ashesi-E-Academic-Advisor/dash1/ASH.php", port=8080, debug=True)
