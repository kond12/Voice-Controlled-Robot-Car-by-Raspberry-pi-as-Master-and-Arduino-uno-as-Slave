while True:
    from speech_recognizer import command
    from tts_ import execute
    from filter_data import filter_results

    command = command()  # create a variable and a calling command function
    print(command)

    try:
        filter_results(command)
    except Exception:
        print('error occured')
        

    

    
        
