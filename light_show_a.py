## Light Show for Homework

from machine import Pin
from time import sleep


leD1 = Pin(10,Pin.OUT)
leD2 = Pin(11,Pin.OUT)
leD3 = Pin(12,Pin.OUT)
leD4 = Pin(13,Pin.OUT)
leD5 = Pin(14,Pin.OUT)
leD6 = Pin(15,Pin.OUT)

delaY1 = .5
delaY2 = .05
delaY3 = 4
delaY4 = .15

try:
    while True:
        ## fast flicker
        for fF in range (10):
            leD1.value(1)
            leD2.value(1)
            leD3.value(1)
            leD4.value(1)
            leD5.value(1)
            leD6.value(1)
                    
            sleep (delaY2)
            
            leD1.value(0)
            leD2.value(0)
            leD3.value(0)
            leD4.value(0)
            leD5.value(0)
            leD6.value(0)
            
            sleep (delaY2)
        
        ## On Solid
        leD1.value(1)
        leD2.value(1)
        leD3.value(1)
        leD4.value(1)
        leD5.value(1)
        leD6.value(1)
        sleep (4)    
        
        for fliC in range (6):
        ## The Flicker
            leD1.value(1)
            leD2.value(1)
            leD3.value(1)
            leD4.value(1)
            leD5.value(1)
            leD6.value(1)
                    
            sleep (delaY1)
            
            leD1.value(0)
            leD2.value(0)
            leD3.value(0)
            leD4.value(0)
            leD5.value(0)
            leD6.value(0)
            
            sleep (delaY1)
            
        ## On Solid
        leD1.value(1)
        leD2.value(1)
        leD3.value(1)
        leD4.value(1)
        leD5.value(1)
        leD6.value(1)
        sleep (delaY3)        
        
        ## Split
        for spliT in range (5):
            leD1.value(0)
            leD2.value(0)
            leD3.value(1)
            leD4.value(1)
            leD5.value(0)
            leD6.value(0)
            sleep(delaY1)
            
            leD1.value(0)
            leD2.value(1)
            leD3.value(0)
            leD4.value(0)
            leD5.value(1)
            leD6.value(0)
            sleep(delaY1)
            
            leD1.value(1)
            leD2.value(0)
            leD3.value(0)
            leD4.value(0)
            leD5.value(0)
            leD6.value(1)
            sleep(delaY1)
            
            ## reverse split
            leD1.value(0)
            leD2.value(1)
            leD3.value(0)
            leD4.value(0)
            leD5.value(1)
            leD6.value(0)
            sleep(delaY1)
            
           
        ## On Solid
        leD1.value(1)
        leD2.value(1)
        leD3.value(1)
        leD4.value(1)
        leD5.value(1)
        leD6.value(1)
        sleep (delaY3)
        
        ## blank all lights
        leD1.value(0)
        leD2.value(0)
        leD3.value(0)
        leD4.value(0)
        leD5.value(0)
        leD6.value(0)
        sleep(.03)
        
        ## Sweeping eye
        for scaN in range (15):
            leD1.value(1)
            sleep (delaY4)
            leD1.value(0)
                        
            leD2.value(1)
            sleep (delaY4)
            leD2.value(0)
            
            leD3.value(1)
            sleep (delaY4)
            leD3.value(0)
            
            leD4.value(1)
            sleep (delaY4)
            leD4.value(0)
            
            leD5.value(1)
            sleep (delaY4)
            leD5.value(0)
            
            leD6.value(1)
            sleep(delaY4)            
            leD6.value(0)
            
            ## Reverse sweep
        
            
            leD5.value(1)
            sleep (delaY4)
            leD5.value(0)
            
            leD4.value(1)
            sleep (delaY4)
            leD4.value(0)
            
            leD3.value(1)
            sleep (delaY4)
            leD3.value(0)
            
            leD2.value(1)
            sleep (delaY4)
            leD2.value(0)
            
            
            
except KeyboardInterrupt:
    leD1.value(0)
    leD2.value(0)
    leD3.value(0)
    leD4.value(0)
    leD5.value(0)
    leD6.value(0)