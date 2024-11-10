# Lesson 11 Scale down potentiometer reading into 16ths.
# instead of turning the potentiometer through the infinite range
# 0 to 65,550 you are now ranging it from 0 to 16.
# creating a more uniform dimming and illuminating effect on the
# human visual spectrum.
# For a more fluid dimming and brightening of the led.
# Paul McWhorter's Pico 11 Lesson https://youtu.be/MCo5nXAKyUU?si=9r7qHtMw8lW-Y-Wa
# Supplies: Pico, 10K potent, 220 Ohm resistor, red led,
# 5 Jumpper wires, and an Ice cold Cafine Beverage.
from machine import Pin, ADC, PWM
from time import sleep 
potPin = 28     # Assign Pin Number for Analog read off of Potent's middle pin.
redLed = 17     # Assign Pin number to variable
potRead = ADC(potPin)     # Get reading from analog signal input
rLed = PWM (Pin(redLed))  # Activate PWM pin for output signal
rLed.freq(1000)     #Frequency of cycles
rLed.duty_u16(0)    # Out puts simulated voltage by
                    # by manipulating duty cycle
try:
    while True:
        potVal = potRead.read_u16()  # Gets Value of Read Pin
        expVal = (16/65535) * potVal # Exponential value for dividing 16 by potVal
        
        brightNess = (2)**expVal # converts the exponential value into the outgoing PWM
                                 # signal back to an ADC Value. 2 is the constant of the
                                 # between the two  exponent values.
                                 # You find the constant by c= (65550**(1/16)
        
        print (expVal,potVal,brightNess)
        rLed.duty_u16(int(brightNess)) # Sends ADC value in the form of volts to the led.
        sleep(.1) # Stops loop from cycling to fast and overwhelming you with the data
                  # being printed to the screen.
        
except KeyboardInterrupt:
    rLed.duty_u16(0)