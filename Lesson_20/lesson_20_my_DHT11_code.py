# ***********************************************************
# Lesson 20 12/12/24
# Paul McWhorter's Rpi Pico W lessons. Lesson 20
# This lesson went arrye. No fault of Paul's or SunFounders.
# The DHT11 sensor has some mfg issues. I believe the IC
# being used for the manufacture of this sensor is
# an inferior performer.
# ***********************************************************
import utime as time
from machine import Pin
from dht import DHT11, InvalidPulseCount

# Declare Constants and Pin Functions
entrY = 0 	# I keep track of each successful sensor reading. I do the same for pulse errors. Then compare them.
pulseErrors = 0 # Count bad pulses
piN = Pin(16, Pin.IN,Pin.PULL_DOWN) # The 'Pin.PULL_DOWN' is not needed, I have tried it both
                                    # ways. It works the same either way. Paul puts it in. 
# Decalre Device names
pwrLt = Pin ('LED',Pin.OUT)
sensor = DHT11(piN)

def cel_to_fahr(temp_celsius):	# Convert Celcius to Fahrenheight  
    temp_fahrenheit = temp_celsius * (9/5) + 32 
    return temp_fahrenheit

pwrLt.value(1) # Turn on Power Indicator Light
time.sleep(1)
try: 	# I like to have a power light that indicates that the pico is on and running something.
        # this try loops kills the power light on the Pico when you stop the program.
    
    # ***Start Main Loop***
    while True:
        
        try: 	# Every so often the sensor throws a bad pulse error, nature of the sensor.
                # To adjust for this SunFounder uses a try/exception loop to reloop the sensor
                # reading until it gives a proper signal.   
            sensor.measure() # Get Temp and Humid readings from sensor
            farNht = cel_to_fahr(sensor.temperature) # Convert celcius to fahrenheit
            entrY = entrY + 1 # Keep a count of read and display loop
            strinG = "Room Temp: {}  °C\nHumidity:    {} %".format(sensor.temperature, sensor.humidity) # Sundfounder's way of printing the data
            # Display Data
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print('Read Sensor #:', entrY, '\nRoom Temp:', farNht, "°F", '\n' + strinG,'\nPulse Errors:', pulseErrors)
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        except InvalidPulseCount as e:
            pulseErrors = pulseErrors +1
            entrY = entrY + 1 	# Keep a count of read and display loop. Added this one because the pulse error
                                # in this exception happens outside of the read and display loop.So we need one here. 
        time.sleep(5)   
    # ***End main Loop***
        
except KeyboardInterrupt:
    pwrLt.value(0) # Turn off power light 