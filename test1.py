"""Control of Arduino over the USB port from pi"""

# USB_PORT = "/dev/ttyUSB0"  # Arduino Uno R3 Compatible
# Arduino Uno WiFi Rev2


# Imports
import serial
import time
from tts_ import execute

# Send commands to Arduino
def moto_(command):
    USB_PORT = "/dev/ttyACM0"  
    usb = serial.Serial(USB_PORT, 115200, timeout=2)
    #usb.write("Hello from Raspberry Pi!\n".encode('utf-8'))
    if "go forward" in command:     # checking condition for voice command
          usb.write(b'go forward')# send command to Arduino
          execute("i am going forward "*2) # speaks what it is doing 
    elif "go back" in command:  # checking condition for voice command
          usb.write(b'go back')  # send command to Arduino uno
          execute("i am going backward "*2)  # speaks what it is doing
    elif "go right" in command:   # checking condition for voice command 
          usb.write(b'go right')  # send command to Arduino uno
          execute("i am going right "*2)  # speaks what it is doing
    elif "go left" in command:     # checking condition for voice command
          usb.write(b'go left')   # send command to Arduino uno
          execute("i am going left "*2)  # speaks what it is doing
    elif "long left" in command:    # checking condition for voice command 
          usb.write(b'long left')  # send command to Arduino uno
          execute("i am taking long left curve"*2) # speaks what it is doing  
    elif "long right" in command:    # checking condition for voice command
          usb.write(b'long right')  # send command to Arduino uno
          execute("i am taking long  right curve"*2) # speaks what it is doing 
    elif "reverse left" in command:    # checking condition for voice command
          usb.write(b'reverse left')  # send command to Arduino uno
          execute("i am taking long   back left curve "*2)  # speaks what it is doing
    elif "reverse right" in command:    # checking condition for voice command
          usb.write(b'reverse right')  # send command to Arduino uno
          execute("i am taking long   back left curve "*2)     
    elif  "stop" in command:     # exit program
          execute("Exiting program.")
          exit()
    else:  # unknown command
        print("Unknown command '" + words + "'.")
    

   
