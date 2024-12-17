# Lesson 20 Temperature and Humidity Sensor

from machine import Pin
import utime as time
from dht import DHT11
dataPin = 16
myPin = Pin (dataPin,Pin.OUT,Pin.PULL_DOWN)
sensor = DHT11(myPin)

while True:
    sensor.measure ()
    temp_C = sensor.temperature # Paul originally wrote 'temp_C = sensor.temperature()'
    hum = sensor.humidity		# Paul originally wrote 'hum = sensor.humidity()'
                                # Both lines would report a float error
    print(temp_C,hum)
    time.sleep(1)