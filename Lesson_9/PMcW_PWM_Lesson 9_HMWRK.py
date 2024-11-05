# Dimmable Light
# Homework Paul McWhorter Lesson 9 Pico W
# https://youtu.be/GXA1Y6lA14A?si=3WBKjpUWdsQdZCy1
# Notes At end of algorithm. 
from machine import PWM, Pin
from time import sleep
pwm_Out = 16      #PWM Pin Variable Assignment
analogOut=PWM(Pin(pwm_Out)) # Declaring pin 16 location as analog.
analogOut.freq (1000)       # Have to assign frequency:
analogOut.duty_u16(0)       # Duty Cycle Max is around 65535'ish

while True:
    myVoltage = float(input('Voltage: ')) #User Inputs Value
    if myVoltage > 3.3:
        print("Error 001: Value To High")
    else:
        pwmVal = (65300/3.30) * myVoltage 
        analogOut.duty_u16(int(pwmVal))
        sleep(.1)
    
# ************************************************************                            
# Frequency the duration of the cycle.
# Duty cycle is How long the voltage\signal is on and off inside
# the frequency cycle. 
# Low Frequency is turning the pin on and off real slow
# High Frequency is turning the pin on and off very fast
# Duty Cycle adjust how long or short the voltage is applied
# inside the frequency cycle, which determins how much or
# how little time the voltage\signal is on and off thus
# simulationg the amount of voltage up or down by how long
# Voltage is on or off.
# ************************************************************