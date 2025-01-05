# Pauls Lesson 20 Humidity and Sensor Data
# This is the best button and humidity sensor set up
from machine import Pin
import utime as time
from dht import DHT11, InvalidPulseCount
pulseS = 0
dataPin = 16
myPin = Pin(dataPin, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(myPin)

butPin = 14
myButton = Pin (butPin, Pin.IN, Pin.PULL_UP)
tempuUnitC = True
buttonState = 1
buttonStateOld = 1
print('My Sensor Data')

while True:
    buttonState = myButton.value()
    if buttonStateOld == 0 and buttonState == 1:
        tempuUnitC =  not tempuUnitC
    try:
        sensor.measure()
    except InvalidPulseCount as e:
        '''
        '''
    tempC = sensor.temperature
    tempF = tempC * 9/5 + 32
    hum = sensor.humidity
    if tempuUnitC == True:
        print("\r", 'Temp= ', tempC,chr(176) + 'C ','Humidity= ',hum,'%',end = '     ')
    if tempuUnitC == False:
        print("\r", 'Temp= ', tempF,chr(176) + 'F ','Humidity= ',hum,'%',end = '')
    time.sleep(.021)
    buttonStateOld = buttonState