import os
import pyttsx3  #  importing already installed package text to speech

engine = pyttsx3.init() #invokes function to reference to pyttsx. engine 

def execute(inputText):
    if True:
        print("text to speech started working") # to know it is working
        output = engine.say(inputText)  #queues a command to speak
        engine.setProperty("rate",170) #queues a command to set engine property
        engine.runAndWait() # permits current comments if all queued comments are empied
        return output       # returns the output
    else:
        output = os.system(inputText)
        return output
   
