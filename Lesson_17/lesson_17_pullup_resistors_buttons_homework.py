from machine import Pin
from time import sleep
btnPin = 17
btnPress = Pin(btnPin,Pin.IN,Pin.PULL_UP) 	# PULL_UP tells the pico to use it's pull up resistor to
leD = Pin(14,Pin.OUT)                       # So we have a constant stable 3.3 volts on and the pico or
leD.value(0)                                # code reacts when it drops to 0. Reverse of normal so to speak.
switch = 'off'	# Set switch starting point
try:
    while True:        
        btnState = btnPress.value()	# Get on or off value of button     
        if btnState == 0 and switch == 'off':	# Was button pushed?
            leD.value(1)
            switch= 'on'
            sleep (.5)	# Gives enough time to get your finger off the button for the next cycle
        elif btnState == 0 and switch == 'on':  # Was button pushed again? Must be 'elif' otherwise if it is an 
            leD.value(0)						# 'if' it will check and find the second argument true as well.
            switch = 'off'
            sleep (.5)	# Gives enough time to get your finger off the button for the next cycle, otherwise it will flash.
        print ('=-=-=-=-=-=-=-=-=-=')
        print ('Light is ' + switch)
        print ('Button Position:',btnState)
        print ('=-=-=-=-=-=-=-=-=-=') 
        sleep(.3)
except KeyboardInterrupt():
    leD.value(0)