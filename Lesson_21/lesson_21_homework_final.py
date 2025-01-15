'''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
A Hansen - 01/14/25
Pauls Lesson 21 Humidity and Sensor Data Everytime you press the
button you must cycle to the next piece of data. It starts out with
temp in C, press button then displays temp in F, then one more push
and it shows humidity, press again and it cycles back to temp from
machine import Pin
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''
from machine import Pin
import utime as time
from dht import DHT11, InvalidPulseCount
timeCycle = .005
bttnPrss = 0
# Sensor Set Up
dataPin = 16
myPin = Pin(dataPin, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(myPin)
# End Sensor set Up
# Button Set Up
butPin = 14
myButton = Pin (butPin, Pin.IN, Pin.PULL_UP)
# End Button Set Up
buttonState = 1
buttonStateOld = 1
print('-=Sensor Data=-')
# Pre Loop Setup ***************
try:
    sensor.measure()
except InvalidPulseCount as e:
    ''' Needed filler for the command routine ''' 
tempC = sensor.temperature
hum = sensor.humidity
print("\r", 'Temp:', tempC,chr(176) + 'C ',end = '   ')
bttnPrss = 1
# End Preloop Setup *****************
while True:
    buttonState = myButton.value()
    try:
        sensor.measure()
    except InvalidPulseCount as e:
        '''Needed to full fill a command routine ''' 
    tempC = sensor.temperature
    tempF = tempC * 9/5 + 32
    hum = sensor.humidity    
    if buttonStateOld == 0 and buttonState == 1:
        if bttnPrss == 0:
            print("\r", 'Temp:', tempC,chr(176) + 'C ',end = '   ')
            bttnPrss = 1
        elif bttnPrss == 1: 
            print("\r", 'Temp:', tempF,chr(176) + 'F ',end = '   ')
            bttnPrss = 2
        elif bttnPrss == 2:
            print ("\r",'Humd:',hum,'%',end = '   ')
            bttnPrss = 0    
    time.sleep(timeCycle)
    buttonStateOld = buttonState