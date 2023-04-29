import wikipedia
from tts_ import execute
import requests,json
from datetime import date,datetime

'''time'''
todat_date=date.today().strftime('%d: %B: %Y')
year = date.today().strftime('%Y')
month = date.today().strftime('%B')
current_time = datetime.now().strftime('%I: %M: %P')
day = datetime.now().strftime('%A')


'''# weather report code

api_key = "62d30130e2b355155d0066ce7ecbc42f"
base_url = "https://openweathermap.org/data/2.5/weather?"
city = "siegen"
complete_url = base_url + "appid" + api_key+ "&q=" + city
response = requests.get(complete_url)
x = response.json()
print(x)

if x["cod"] != "404":
    data = x["main"]
    current_temp = int(data["temp"])-273
    current_pressure = data["pressure"]
    current_humidity = data["humidity"]
    weather_value = x["weather"]
    weather_description = [0]["description"]

else:
    print("network error!!")'''
    

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

'''def weather_(command):
    if "temperature" in command:
        execute(f"""current temperature is,{current_temp} "degree celsius" """)

    elif "humidity" in command:
       execute(f"'current humidity is,{current_humidity}  70 percent'")
    elif "pressure" in command:
       execute(f"""current humidity is,{current_pressure} " hecto pascals" """)
    elif "weather" in command:
       execute(f"""{weather_description} """)
    else:
        execute("can you repeat?")'''

             
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
                 

    
        

        
        
        
        
