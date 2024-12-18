# HomeWork Lesson 20 Temperature and Humidity Sensor
# Press Button and it changes between Celcius and fahrenheight.
import utime as time
from machine import Pin
from dht import DHT11, InvalidPulseCount

# Declare Constants and Pin Functions
switch_State = 'celcius'
entrY = 0 	# I keep track of each successful sensor reading. I do the same for pulse errors. Then compare them.
pulseErrors = 0 # Count bad pulses
piN = Pin(16, Pin.IN,Pin.PULL_DOWN) # The 'Pin.PULL_DOWN' is not needed, I have tried it both
                                    # ways. It works the same either way. Paul puts it in.
# *** Declare Push Button***
btnPin = 14
btnPress = Pin(btnPin,Pin.IN,Pin.PULL_UP)
# *** End Push Button Set Up***

# Decalre power light and temp\hum sensor
pwrLt = Pin ('LED',Pin.OUT)
sensor = DHT11(piN)

# ***define fucntion to convert Celcius to Fahrenheight ***
def cel_to_fahr(temp_celsius):	# Convert Celcius to Fahrenheight  
    temp_fahrenheit = temp_celsius * (9/5) + 32 
    return temp_fahrenheit

pwrLt.value(1) # Turn on Power Indicator Light
try: 	# I like to have a power light that indicates that the pico is on and running something.
        # this try loops kills the power light on the Pico when you stop the program on the computer.
    
    # ***Start Main Loop***
    while True:
        btnState = btnPress.value()
        
        try: 	# Every so often the sensor throws a bad pulse error, nature of the sensor.
                # To adjust for this SunFounder uses a try/exception loop to reloop the sensor
                # reading until it gives a proper signal.   
            sensor.measure() # Get Temp and Humid readings from sensor
            farNht = cel_to_fahr(sensor.temperature) # Convert celcius to fahrenheit
            cel_Temp = sensor.temperature # Get a constant for celcius temp, easier for print statement. 
            humiD = sensor.humidity # Humidity value in %
            
            # Button Logic Resolution
            if switch_State == 'celcius' and btnState == 0:
                switch_State = 'fahrn'
            elif switch_State == 'fahrn' and btnState == 0:
                switch_State = 'celcius'
            # Display Information Logic
            if switch_State == 'fahrn':
                print('\r','Temperature:', int(farNht), chr(176) + 'F','  Humidity:', humiD,'%', end = '')
            elif switch_State == 'celcius':
                print('\r','Temperature:', int(cel_Temp), chr(176) + 'C','  Humidity:', humiD,'%', end = '')
        except InvalidPulseCount as e: # without this the program crashes due to pulse errors.
            pulseErrors = pulseErrors +1
        time.sleep(.21)   
    # ***End main Loop***
except KeyboardInterrupt:
    pwrLt.value(0) # Turn off power light 