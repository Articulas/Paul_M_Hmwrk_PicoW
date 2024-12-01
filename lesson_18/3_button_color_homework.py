# ***************************************************************************************
# Lesson 18 Homework                                                                    * 
# Using an RGB, and 3 buttons (one red,blue,green).                                     *
# The idea is if you push a green button the bulb lights up green, red and blue thusly. *
# 1 RGB LED, 3 Push Buttons, 1 220ohm resistor, Pico MC Board, Jumper wires,            *
# ***************************************************************************************    
# RGB Pins Red 15, Green 14, Blue 13 Must all be PWM                                    * 
# Buttons 1,2, and 3 must all be set to input and a pull up resistor.                   *
# Lights must activate and deactivate on the button's release!                          *
# ***************************************************************************************
from machine import Pin,PWM
from time import sleep
# Set Up RGB LED pins
rLEDpin = 13
gLEDpin = 14
bLEDpin = 15
# Declair color key word and activate it them as PWM pins. 
rColor = PWM (Pin(rLEDpin))
gColor = PWM (Pin(gLEDpin))
bColor = PWM (Pin(bLEDpin))
# Set up frequeny of signals for each color pin.
rColor.freq(1000)
gColor.freq(1000)
bColor.freq(1000)
# Set up button pins
rbutPin = 16
gbutPin = 17
bbutPin = 22
# Declare buttons as inputs w/ pull up resistor
rButton = Pin(rbutPin,Pin.IN,Pin.PULL_UP)
gButton = Pin(gbutPin,Pin.IN,Pin.PULL_UP)
bButton = Pin(bbutPin,Pin.IN,Pin.PULL_UP)
# Set constant logic variable
rbtnStatNow = 1
rbtnStatOld = 1
gbtnStatNow = 1
gbtnStatOld = 1
bbtnStatNow = 1
bbtnStatOld = 1
rLEDstat=False
gLEDstat=False
bLEDstat=False
# Make sure all the colors are off.
rColor.duty_u16(0)
gColor.duty_u16(0)
bColor.duty_u16(0)
# Primary Algorithm 
while True:
    # Get the button state (is it on or off, 0 or 1)
    rbtnStatNow = rButton.value()
    gbtnStatNow = gButton.value()
    bbtnStatNow = bButton.value()
    # test for button push
    if rbtnStatNow == 1 and rbtnStatOld == 0: 	# Changing the position of the 0 and 1
        rLEDstat = not rLEDstat					# changes the button behaviour. This way
        rColor.duty_u16(65550)					# activates switch pressed down, the other activates switch when it is let up.
        gColor.duty_u16(0)
        bColor.duty_u16(0)
    elif gbtnStatNow == 1 and gbtnStatOld ==0:
        gLEDstat = not gLEDstat
        rColor.duty_u16(0)
        gColor.duty_u16(65550)
        bColor.duty_u16(0)
    elif bbtnStatNow == 1 and bbtnStatOld == 0:
        bLEDstat = not bLEDstat
        rColor.duty_u16(0)
        gColor.duty_u16(0)
        bColor.duty_u16(65550)
    # Set up logic constants for next cycle of loop
    rbtnStatOld = rbtnStatNow
    gbtnStatOld = gbtnStatNow
    bbtnStatOld = bbtnStatNow
    sleep(.1)
    print (rbtnStatOld,rbtnStatNow,gbtnStatOld,gbtnStatNow,bbtnStatOld,bbtnStatNow)