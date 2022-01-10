import pyttsx3
import pywhatkit 
import speech_recognition as sr
import datetime

# speech recognition  basically this is going to listen for voice input using the python speech recognition library.
listener = sr.Recognizer()
engine = pyttsx3.init()# initializes python text to speach engine

# if you wanted to change the voice...
#declared variable
voices = engine.getProperty('voices')

# telling the engine to set the paroperty in accordance to the library used, reference the docs
# engine.setProperty('voice', voices[anyInt].id)
engine.say('i am the friendly robotic automata, now conceptualized, call me franc for short, my creator is eeno alexander, i am awaiting command')

def speak(text):
    #this is what frank will say when activated intially by his name
    engine.say(text)
    engine.runAndWait()

def prompt_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source) # this is listening for  a source which would be the microphone listening for voice input
            command = listener.recognize_google(voice) # uses google voice 
            command = command.lower()#computers like lowercase letters and it makes it easier for it to interpret what is being said.
            if 'frank' in command:
                command = command.replace('franc', '') #removes francs from the command so it isnt said or printed to the console as part of the query.
                print(command)
    except:
        pass
    return command

# we are calling the above function and giving the command below
# will take the command function from user from the prompt_command function above.
def user_command():
    command = prompt_command()
    print(command)
    # for playing songs
    if 'play' in command:
        song = command.replace('play, i want to listen to, put on some, i want to listen to some,', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
            
        
        
while True:
    user_command
