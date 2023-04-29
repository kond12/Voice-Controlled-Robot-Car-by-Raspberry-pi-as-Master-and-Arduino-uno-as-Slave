from datetime import date,datetime
from tts_ import execute

'''time'''
todat_date=date.today().strftime('%d: %B: %Y')
year = date.today().strftime('%Y')
month = date.today().strftime('%B')
current_time = datetime.now().strftime('%I: %M: %P')
day = datetime.now().strftime('%A')

def time_(command):
     command.lower()
     if "time" in command:
         execute(f"{current_time}")
     elif "date" in command:
         execute(f"{current_date}")
     elif "year" in command:
         execute(f"{year}")
     elif "month" in command:
         execute(f"{month}")
     elif "day" in command:
         execute(f"{day}")
     else:
        pass
                 
