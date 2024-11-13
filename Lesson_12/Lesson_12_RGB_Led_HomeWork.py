# Lesson 12 Homework RGB LED
# Paul's Pico Lessons here https://youtu.be/yZkx-KWbATY?si=h8FRv9evhzpydnjQ
# RGB LED display basic colors when they are entered by the user.
# Prompt User for red green blue cyan magenta yellow orange white
from machine import Pin,PWM
from time import sleep
rPin = 16
gPin = 17
bPin = 18
rClr = PWM(Pin(rPin))
gClr = PWM(Pin(gPin))
bClr = PWM(Pin(bPin))
deLay = .5
#Setup
leD = machine.Pin('LED', Pin.OUT)  # Replace 0 with your LED pin number
leD.value(1)  # Power Indication Light Now ON
rClr.freq(1000)
gClr.freq(1000)
bClr.freq(1000)
rClr.duty_u16(0)
gClr.duty_u16(0)
bClr.duty_u16(0)

# Main Loop
try:
    while True:
        coLor = input("What Color do You Choose(red green blue cyan magenta purple yellow orange white):")
        
        if coLor == ("orange"):
            #print ("orange")    
            rBright = 65550
            gBright = 8000
            bBright = 0
        elif coLor == ("yellow"):
            rBright = 65550
            gBright = 18000
            bBright = 0
        elif coLor == ("blue"):
            rBright = 0
            gBright = 0
            bBright = 65550
        elif coLor == ("purple"):
            rBright = 65550
            gBright = 0
            bBright = 65550
        elif coLor == ("green"):
            rBright = 0
            gBright = 65550
            bBright = 0
        elif coLor == ("red"):
            rBright = 65550
            gBright = 0
            bBright = 0
        elif coLor == ("cyan"):
            rBright = 0
            gBright = 45000
            bBright = 45000
        elif coLor == ("magenta"):
            rBright = 60000
            gBright = 0
            bBright = 30000
        elif coLor == ("white"):
            rBright = 65550
            gBright = 65550
            bBright = 65550
        else:
            print ("Error Please Retry")
            sleep (2)
            rBright = 0
            gBright = 0
            bBright = 0
           
        rClr.duty_u16(rBright)
        bClr.duty_u16(bBright)
        gClr.duty_u16(gBright)
        sleep (deLay)

except KeyboardInterrupt:
    leD.value(0)
    rClr.duty_u16(0)
    bClr.duty_u16(0)
    gClr.duty_u16(0)