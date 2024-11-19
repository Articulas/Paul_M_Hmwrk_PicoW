# 11/18/24 
# Lesson 15 Home work https://youtu.be/Fx7m-zmyVaY?si=DC4TzzjeAjFOZgkZ
# Program must ask for number of colors to display, and then ask for
# The colors you want displayed.
# for loops, while loops
# Red, Green, Blue, Cyan, Magenta, Orange, Purple, White, Off
from machine import Pin,PWM
from time import sleep

rPin = 13
gPin = 14
bPin = 15
# Decalre color related pins and set frequency of signal
rColor = PWM (Pin(rPin))
gColor = PWM (Pin(gPin))
bColor = PWM (Pin(bPin))
rColor.freq(1000)
gColor.freq(1000)
bColor.freq(1000)
# Reset colors to zero
rColor.duty_u16(0)
gColor.duty_u16(0)
bColor.duty_u16(0)

deLay = 2

while True:
    coLors = []    
# Step 1 Get Number of Colors input
    print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    numColors = input('Number of Colors: ')
    print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
# Step 2 Get each individual color input
    print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    for i in range (int(numColors)):
        chColors = input ('Color choice #' + str(i + 1) + ' ')
        #avaiColor ['red','blue','green','cyan','magenta','purple','white,'off']
        coLors.append(chColors)    
# Step 3 display said colors with RGB LED
    print(coLors)
    print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    
    for i in range (int(numColors)):
        
        if coLors[i] == ("orange"):
            rBright = 65550
            gBright = 8000
            bBright = 0
        elif coLors[i] == ("yellow"):
            rBright = 65550
            gBright = 18000
            bBright = 0
        elif coLors[i] == ("blue"):
            rBright = 0
            gBright = 0
            bBright = 65550
        elif coLors[i] == ("purple"):
            rBright = 65550
            gBright = 0
            bBright = 65550
        elif coLors[i] == ("green"):
            rBright = 0
            gBright = 65550
            bBright = 0
        elif coLors[i] == ("red"):
            rBright = 65550
            gBright = 0
            bBright = 0
        elif coLors[i] == ("cyan"):
            rBright = 0
            gBright = 45000
            bBright = 45000
        elif coLors[i] == ("magenta"):
            rBright = 60000
            gBright = 0
            bBright = 30000
        elif coLors[i] == ("white"):
            rBright = 65550
            gBright = 65550
            bBright = 65550
        elif coLors[i] == ('off'):
            rBright = 0
            gBright = 0
            bBright = 0        
        else:
            print ("Error Please Retry")
            sleep (2)
            rBright = 0
            gBright = 0
            bBright = 0
        
        rColor.duty_u16(rBright)
        bColor.duty_u16(bBright)
        gColor.duty_u16(gBright)
        sleep (deLay)
        
        rColor.duty_u16(0)
        bColor.duty_u16(0)
        gColor.duty_u16(0)
    