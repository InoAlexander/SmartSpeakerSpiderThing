import pyttsx3
import speech_recognition as sr


# speech recognition  basically this is going to listen for voice input using the python speech recognition library.
listener = sr.Recognizer()
engine = pyttsx3.init()# initializes python text to speach engine

#this is what frank will say when activated intially by his name
engine.say('I am franc your eternal friend, what can i do to be of service')
engine.say('i am the friendly robotic automata now conceptualized, but you can call me franc for short, awaiting command')

try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source) # this is listening for  a source which would be the microphone listening for voice input
        command = listener.recognize_google(voice) # uses google voice 
        command = command.lower()#computers like lowercase letters and it makes it easier for it to interpret what is being said.
        if 'frank' in command:

            print(command)
except:
    pass
