// USB - USB.ino
//
// Description:
// Executes commands retrieved from serial (USB) port.
//
// Created by John Woolsey on 12/17/2019.
// Copyright (c) 2019 Woolsey Workshop.  All rights reserved.


#include <Wire.h>
#include <EVShield.h>
#define SH_Speed_Full 90
#define SH_Speed_Medium 62
#define SH_Speed_Slow 54
#define SH_CONTROL_SPEED 
#define SH_Motor_both 
// setup for this example:
// attach external power to EVShield.
// attach 2 motors to motor ports 
// Open the Serial terminal to view.

EVShield          evshield(0x34,0x36);



void setup()
{
    Serial.begin(115200);      // start serial for output
    delay(1);                  // wait  1 milli seconds, allowing time to
                               // activate the serial monito
    
                              
    long degrees;
    long rotations ;            // Define variable rotations and set  equal to 90
    char   str[40];

    evshield.init( SH_HardwareI2C );

    //
    // Wait until user presses GO button to continue the program
    //
    while (!evshield.getButtonState(BTN_GO)) {
        if (millis() % 1000 < 0.001) {
            Serial.println("Press GO button to continue");
        }
    }

    //
    // reset motors.
    //
    evshield.bank_a.motorReset();
    evshield.bank_b.motorReset();
    
}

void loop() 
{
       
    long            rotations ; 
    long control;
    #include <EVShield.h>
    #define SH_CONTROL_SPEED     
    #define SH_CONTROL_RAMP      
    #define SH_CONTROL_RELATIVE 
    char            str[40];
  
   // Drive both motor  forward  for a specific number of rotations
   if (Serial.available()) {                  // check for incoming serial data
      String command = Serial.readString();  // read command from serial port
       // Serial.print("You sent me: ");
      if (command == "go forward") {         // checking condition to execute forward motion 
          long       degrees = 2052;          // no of rotations
          delay(1);
          evshield.bank_a.motorStartBothInSync();
          sprintf(str, "Both Motors Forward %d Rotations", rotations);
          Serial.println(str);
          str[0] = '\0';
          evshield.bank_a.motorRunDegrees(SH_Motor_Both, 
                     SH_Direction_Reverse,
                     SH_Speed_Medium, 
                     degrees, 
                     SH_Completion_Wait_For,
                     SH_Next_Action_BrakeHold);
  
      } else if (command == "go back") {  // Drive both motor  backward for a specific number of rotations
          float            degrees = 2052;
         delay(1);
         evshield.bank_a.motorStartBothInSync();
         sprintf(str, "Both Motors Reverse %d Rotations", rotations);
         Serial.println(str);
         str[0] = '\0';
         evshield.bank_a.motorRunDegrees(SH_Motor_Both, 
                     SH_Direction_Forward,
                     SH_Speed_Medium, 
                     degrees, 
                     SH_Completion_Wait_For,
                     SH_Next_Action_BrakeHold);

      } else if (command == "go right") {   // Drive left motor  forward for a specific number of rotations
          long            degrees =360;
          delay(1);
          sprintf(str, "Motor 2 Forward %d Rotations", rotations);
          Serial.println(str);
          str[0] = '\0';
          evshield.bank_a.motorRunDegrees(SH_Motor_2, 
                     SH_Direction_Reverse,
                     SH_Speed_Slow,
                     degrees, 
                     SH_Completion_Wait_For,
                     SH_Next_Action_BrakeHold);             
       } else if (command == "go left") {     // Drive right motor  forward for a specific number of rotations                   
         long            degrees = 360;
         delay(1);
         sprintf(str, "Motor 1 Forward %d Rotations", rotations);
         Serial.println(str);
         str[0] = '\0';
         evshield.bank_a.motorRunDegrees(SH_Motor_1, 
                     SH_Direction_Reverse,
                     SH_Speed_Slow,
                     degrees, 
                     SH_Completion_Wait_For,
                     SH_Next_Action_BrakeHold);
         }else if (command == "long right") {  // Drive both motors with different speed for a specific number of rotations for long left curve
          long            degrees;
          delay(1);
          sprintf(str, "Motor 2 Forward %d Rotations", rotations);
          Serial.println(str);
          str[0] = '\0';
          evshield.bank_a.motorRunDegrees(SH_Motor_2, 
                     SH_Direction_Reverse, 
                     SH_Speed_Medium,
                     degrees=3060, 
                     SH_Completion_Dont_Wait,
                     SH_Next_Action_BrakeHold);          
           evshield.bank_a.motorRunDegrees(SH_Motor_1, 
                     SH_Direction_Reverse,
                     SH_Speed_Slow,
                     degrees=2678, 
                     SH_Completion_Wait_For,
                     SH_Next_Action_BrakeHold);
         } else if (command == "long left") {  // Drive both motors with different speed for a specific number of rotations for long right curve 
          long            degrees ;
          delay(1);
          sprintf(str, "Motor 2 Forward %d Rotations", rotations);
          Serial.println(str);
          str[0] = '\0';
          evshield.bank_a.motorRunDegrees(SH_Motor_2, 
                     SH_Direction_Reverse,
                     SH_Speed_Slow,
                     degrees = 2678,
                     SH_Completion_Dont_Wait,
                     SH_Next_Action_BrakeHold);          
           evshield.bank_a.motorRunDegrees(SH_Motor_1, 
                     SH_Direction_Reverse,
                     SH_Speed_Medium,
                     degrees= 3060,
                     SH_Completion_Wait_For,
                     SH_Next_Action_BrakeHold); 
          } else if (command == "reverse right") {  // Drive both motors with different speed for a specific number of rotations for long left reverse curve
         long            degrees;
         delay(1);
         sprintf(str, "Motors 1 Reverse %d Rotations", rotations);
         Serial.println(str);
         str[0] = '\0';
         evshield.bank_a.motorRunDegrees(SH_Motor_1, 
                     SH_Direction_Forward,
                      SH_Speed_Slow,
                     degrees = 2678, 
                     SH_Completion_Dont_Wait,
                     SH_Next_Action_BrakeHold);
         evshield.bank_a.motorRunDegrees(SH_Motor_2, 
                     SH_Direction_Forward,
                    SH_Speed_Medium,
                     degrees=3060,
                     SH_Completion_Wait_For,
                     SH_Next_Action_BrakeHold); 
        } else if (command == "reverse left") {  // Drive both motors with different speed for a specific number of rotations for long right reverse curve
         long            degrees;
         delay(1);
         sprintf(str, "Motors 1 Reverse %d Rotations", rotations);
         Serial.println(str);
         str[0] = '\0';
         evshield.bank_a.motorRunDegrees(SH_Motor_2, 
                     SH_Direction_Forward,
                      SH_Speed_Slow,
                     degrees = 2678,
                     SH_Completion_Dont_Wait,
                     SH_Next_Action_BrakeHold);
         evshield.bank_a.motorRunDegrees(SH_Motor_1, 
                     SH_Direction_Forward,
                     SH_Speed_Medium,
                     degrees=3060, 
                     SH_Completion_Wait_For,
                     SH_Next_Action_BrakeHold); 
        } 
   }
}

