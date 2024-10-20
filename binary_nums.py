## Binary Number Study
## Project: Make light display that counts in binary 0 thru 15.
## 4 LEDs, 4 Resistors, 4 Gio Pins, 1 Ground
from machine import Pin
from time import sleep
poS1 = Pin(15,Pin.OUT)
poS2 = Pin(14,Pin.OUT)
poS4 = Pin(13,Pin.OUT)
poS8 = Pin(12,Pin.OUT)
delaY =1.5
oN = 1
ofF = 0

try:
    while True:
        ## 0000
        poS1.value(ofF)
        poS2.value(ofF)
        poS4.value(ofF)
        poS8.value(ofF)
         
        sleep(delaY)
        
        ## 0001
        poS1.value(oN)
        poS2.value(ofF)
        poS4.value(ofF)
        poS8.value(ofF)
        
        sleep(delaY)
        
        ## 0010
        poS1.value(ofF)
        poS2.value(oN)
        poS4.value(ofF)
        poS8.value(ofF)
        
        sleep(delaY)
        
        ## 0011
        poS1.value(oN)
        poS2.value(oN)
        poS4.value(ofF)
        poS8.value(ofF)
            
        sleep(delaY)
        
        ## 0100
        poS1.value(ofF)
        poS2.value(ofF)
        poS4.value(oN)
        poS8.value(ofF)
            
        sleep(delaY)
        
        ## 0101
        poS1.value(oN)
        poS2.value(ofF)
        poS4.value(oN)
        poS8.value(ofF)
            
        sleep(delaY)
        
        ## 0110
        poS1.value(ofF)
        poS2.value(oN)
        poS4.value(oN)
        poS8.value(ofF)
            
        sleep(delaY)
        
        ## 0111
        poS1.value(oN)
        poS2.value(oN)
        poS4.value(oN)
        poS8.value(ofF)
            
        sleep(delaY)
        
        ## 1000
        poS1.value(ofF)
        poS2.value(ofF)
        poS4.value(ofF)
        poS8.value(oN)
            
        sleep(delaY)
        
        ## 1001
        poS1.value(oN)
        poS2.value(ofF)
        poS4.value(ofF)
        poS8.value(oN)
            
        sleep(delaY)
        
        ## 1010
        poS1.value(ofF)
        poS2.value(oN)
        poS4.value(ofF)
        poS8.value(oN)
            
        sleep(delaY)
        
        ## 1011
        poS1.value(oN)
        poS2.value(oN)
        poS4.value(ofF)
        poS8.value(oN)
            
        sleep(delaY)
        
        ## 1100
        poS1.value(ofF)
        poS2.value(ofF)
        poS4.value(oN)
        poS8.value(oN)
            
        sleep(delaY)
        
        ## 1101
        poS1.value(oN)
        poS2.value(ofF)
        poS4.value(oN)
        poS8.value(oN)
            
        sleep(delaY)
        
        ## 1110
        poS1.value(ofF)
        poS2.value(oN)
        poS4.value(oN)
        poS8.value(oN)
            
        sleep(delaY)
        
        ## 1111
        poS1.value(oN)
        poS2.value(oN)
        poS4.value(oN)
        poS8.value(oN)
            
        sleep(delaY)
        
except KeyboardInterrupt:
    poS1.value(ofF)
    poS2.value(ofF)
    poS4.value(ofF)
    poS8.value(ofF)      