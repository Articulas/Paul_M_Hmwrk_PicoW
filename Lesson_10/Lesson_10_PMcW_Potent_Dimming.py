# ************************************************
# Dimmable light 2: Dimming with Potentiometer
# Homework Lesson 10 Paul McWhorter's Pico W Lesson
# Pauls Lesson: https://youtu.be/DJhoUklKidc?si=2u1hpCtTVvkHBoot
# ************************************************
import machine
from time import sleep
from machine import PWM
from machine import Pin
# Variables 
readPin = 28
sendPin = 16
# Declare Pins
myPot = machine.ADC (readPin) # Set up pin to read from potentiometer
analogOut = PWM(Pin(sendPin)) # declair sending pin
analogOut.freq(1000) #frequency of signal
analogOut.duty_u16(0) #Duty cycle set to 0

while True:
    potVal = myPot.read_u16() # Get Potentiometer Pin Reading
    volTage = (3.3/65375) * potVal-(160*3.3/65375)
    outVolts = float(volTage)
    pwmVal = (65375/3.3) * outVolts
    if pwmVal < 0:
        pwmVal = 0
    analogOut.duty_u16(int(pwmVal))
    print("Digital Input Value: ",potVal)
    print ("Digital Output Value: ", pwmVal)
    print ("Volts: ",volTage,"v")
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    sleep (.1)