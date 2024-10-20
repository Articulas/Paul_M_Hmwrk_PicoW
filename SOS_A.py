## S.O.S Signal
## Paul McWhorter HW Assmnt Lesson2
## Note: I am a licensed amateur radio operator. KE2DIR. www.ke2dir.com
## the length of dashes and does depend on the speed at which you can key the keyer.
## Most are between 15 and 25 word per minute.
## **IT IS IMPERATIVE THAT THE DASH IS 3 TIMES LONGER THAN THE DOT*
## At 20 WPM the dot is about 6 millisecods making the dash 18 milliseconds.
## For the purpose of everyone being able to see what is happening I am slowing things down

from machine import Pin
from time import sleep
diT = .08
dA = .18
spcE= .35
leD = Pin(15, Pin.OUT)
wdBK = 2
try:
    while True:
        ## Pause between words
        leD.value(0)
        sleep(wdBK)
        ## Makes S
        for s in range(3):
            leD.value(1)
            sleep(diT)
            leD.value(0)
            sleep(diT)
        ## pause before next letter    
        leD.value(0)
        sleep(spcE)
        ## Makes O
        for o in range (3):
            leD.value(1)
            sleep (dA)
            leD.value(0)
            sleep(dA)
        ## pause before next letter
        leD.value(0)
        sleep(spcE)
        ## Makes second S 
        for sx in range(3):
            leD.value(1)
            sleep(diT)
            leD.value(0)
            sleep(diT)    
except KeyboardInterrupt:
    leD.value(0)  # Turn off the LED when stopping                    