#!/usr/bin/env python3

import serial

if __name__ == '__main__':
           ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
           ser.flush()
      while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)


        
#!/usr/bin/env python3
"""Control an Arduino over the USB port."""

# USB_PORT = "/dev/ttyUSB0"  # Arduino Uno R3 Compatible
USB_PORT = "/dev/ttyACM0"  # Arduino Uno WiFi Rev2


# Imports
import serial
import time
import speech_recognition as sr
# Main

# Connect to USB serial port at 115200 baud
def moto_(command):
try:
   usb = serial.Serial(USB_PORT, 115200, timeout=2)
except:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print("Exiting program.")
   exit()

# Send commands to Arduino
r = sr.Recognizer()
mic = sr.Microphone()
while True:
    print("Enter a voice command from the mic to send to the Arduino.")
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)
    
    if words == "forward":  # read Arduino A0 pin value
          usb.write(b'forward')  # send command to Arduino
          print("motor1 forward")
    elif words == "backward":  # turn on Arduino LED
          usb.write(b'backward')  # send command to Arduino
          print("motor1 backward")
    elif words == "right":  # turn off Arduino LED
          usb.write(b'left')  # send command to Arduino
          print("motor2 forward.")
    elif words == "left":  # turn off Arduino LED
          usb.write(b'rigth')  # send command to Arduino
          print("motor2 backward.")
    elif words == "go":  # turn off Arduino LED
          usb.write(b'go')  # send command to Arduino
          print("motor both forward.")           
    elif words == "stop":  # exit program
          print("Exiting program.")
          exit()
    else:  # unknown command
      print("Unknown command '" + words + "'.")
    
