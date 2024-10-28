# Lesson 6 Homework
# Hardware: 1 Pico, 1 Breadboard, 3 LEDs (Red,Green,Yellow ),
#           Assrted Patch Wires, Potentiometer.
#         !!!Cup of ice coffee; Black No sugar!!!
# If potentiometer is all the way to the left the read value
# should be 0, All the way to the right should be 100
# If Value is 0 to 79 Green Light
# If Value is 80 to 94 Yellow Light
# If value is 95 to 100 Red Light
from machine import Pin
from time import sleep
yeL = 17
grN = 18
reD = 16
oN=1
ofF=0
yleD = machine.Pin(yeL, Pin.OUT)
gleD = machine.Pin(grN, Pin.OUT)
rleD = machine.Pin(reD, Pin.OUT)
knoB = 28 # Pin location 34

digi_rD = machine.ADC(knoB) # Read Analog Digital Converter. Read Value

try:
    while True:
        # The Math 
        digi_vaL = digi_rD.read_u16() # Get Value from digi_rD
        voltage=(3.3/65375)*digi_vaL - (160*3.3/65375)
        percent_vaLb = (digi_vaL * 100) / 65535
        # Cleaning up the display data. 
        if percent_vaLb < 1: # 0 out power level: #smooths out voltage fluctuation. 
            percent_vaLb = 0
        if voltage <= .0001: # 0 out any voltage less than .0001
            voltage = 0
        
        print ("Power Level: ",percent_vaLb)
        print("Digital Volt Reading: ",digi_vaL)
        print("Actual Voltage: ",voltage,"v")
        print ("*****************************")
        
        if percent_vaLb <= 79.999: # Light logic decision 1
            gleD.value(oN)
            
        if percent_vaLb >= 80 and percent_vaLb <= 94.999: #Light logic decision 2
            yleD.value(oN)
            
        if percent_vaLb >= 95 and percent_vaLb <=100: #Light logic decision 3
            rleD.value(oN)
            
        sleep (.5) 
        rleD.value(ofF) # Reset Lights
        yleD.value(ofF)
        gleD.value(ofF)

except KeyboardInterrupt:
    rleD.value(ofF)
    yleD.value(ofF)
    gleD.value(ofF)