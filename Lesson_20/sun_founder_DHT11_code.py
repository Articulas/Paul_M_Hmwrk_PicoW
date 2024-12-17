from machine import Pin
import utime as time
from dht import DHT11, InvalidPulseCount

pin = Pin(16, Pin.IN)
sensor = DHT11(pin)
time.sleep(5)  # initial delay

def cel_to_fahr(temp_celsius): 
    temp_fahrenheit = temp_celsius * (9/5) + 32 
    return temp_fahrenheit

while True:
    try:
        sensor.measure()
        farNht = cel_to_fahr(sensor.temperature)
        print ("Temperature: " + str(farNht) + "°F")
        string = "Temperature: {}°C\nHumidity: {} %".format(sensor.temperature, sensor.humidity)
        print(string)
        time.sleep(4)

    except InvalidPulseCount as e:
        print('Bad pulse count - retrying ...')