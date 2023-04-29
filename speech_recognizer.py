import speech_recognition as sr #importing speech recognition module
r = sr.Recognizer()             # calling speech recognition       
mic = sr.Microphone()          # use microphone as default audio source

def command():                 # defining a function
    with mic as source:
        r.adjust_for_ambient_noise(source) #adjust source noise
        try:
            print("listening.......")

            audio = r.listen(source)  # listen to speech and extract it into audio data
            command_ = r.recognize_google(audio)  # google api to recognise and store data of audio

        except sr.UnknownValueError:
            command_ = "Mic Error"
            print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
    return command_
