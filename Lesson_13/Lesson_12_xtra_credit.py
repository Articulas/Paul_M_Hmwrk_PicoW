# Adam H - 11/13/2024
# Lesson 13 Extra Credit Paul McWhorter's Pico W Lessons
# 3 potentiometers: Each one assigned to Red, Green, and Blue.
# When you turn a potentiometer it makes the assigned color brighter or dimmer
# Thus allowing you to mix the 3 RGB  colors with the potentiomters.
# Parts List: 3 10K Potentiometers, 3 220ohm resistors, 1 RGB bulb, 6 jumper wires, 1 pico and usb
from machine import Pin, PWM, ADC
from time import sleep
# Pin Assignment
rPotpin = 28
gPotpin = 27
bPotpin =26
rLed = 15
gLed = 14
bLed = 13
# GPIO Type Declaration (set up signal receive and send pins)
rPot_val = ADC(rPotpin)
gPot_val = ADC(gPotpin)
bPot_val = ADC(bPotpin)
rSend = PWM (Pin(rLed))
gSend = PWM (Pin(gLed))
bSend = PWM (Pin(bLed))
# Set Frequency of Signals being sent
rSend.freq(1000)
bSend.freq(1000)
gSend.freq(1000)

while True:
    # Get Potentiomter Values
    redVal = rPot_val.read_u16()
    greenVal = gPot_val.read_u16()
    blueVal = bPot_val.read_u16()
    # Since the Potentiometers still alow trace amounts of electricity
    # through it is never 0 and the light is never actually off.
    # The if then logic corrects that    
    if redVal < 180:
        redVal = 0
    if greenVal < 180:
        greenVal = 0
    if blueVal < 180:
        blueVal = 0
    # Send PWM Valus to LED
    print (redVal,greenVal,blueVal)
    rSend.duty_u16(int(redVal))
    gSend.duty_u16(int(greenVal))
    bSend.duty_u16(int(blueVal))
    sleep(.1)