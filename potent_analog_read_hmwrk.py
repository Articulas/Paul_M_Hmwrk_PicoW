# Paul McWhorters Pico Lesson 5 Homework
# https://youtu.be/ODWwErH_iGA?si=67mKYTVGi-qRjVIQ
# Potentiometer Lesson 5
import machine
from time import sleep
potPin=28
myPot=machine.ADC(potPin) #analog digital converter reading

while True:
    potVal = myPot.read_u16() #Read Potentiometer value
    voltage=(3.3/65375)*potVal-(160*3.3/65375) 	# Paul's formula * My base reading
                                                # was different because I used a
                                                # different potentiometer. My formula is
                                                # adjusted to that
    spwR = 3.3 - voltage
    rRatio = (spwR * 100) / 3.3
    print ("Digital Voltage: ",potVal)
    print ("Analog Voltage: ",voltage)
    print ("Resistance Strength Ratio (0-100): ",rRatio)
    print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    sleep (1)
