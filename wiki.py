import wikipedia
from tts_ import execute

def wiki_(command):
    formatted_command = ""
    #for word in command:
        #formatted_command += f"{word}"

    #command = formatted_command[:-1]
    command.lower()
    print(command)

    command = command.replace("know","")
    command = command.replace("about","")
    command = command.replace("to","")    
    command = command.replace("what","")
    command = command.replace("is","")
    command = command.replace("who","")
    command = command.replace("when","")    
    command = command.replace("me","")
    command = command.replace("tell","")
    command = command.replace("did","")
    command = command.replace("want","")    
    command = command.replace("do","")
    print(command)

    data = wikipedia.summary(command,sentences = 3)
    execute(data)
