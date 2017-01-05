#Read the temperature from a thermocouple

#The quickest the thermocouple can be queried is once every 0.25 seconds (or something like it)
from max6675 import MAX6675, MAX6675Error

# Selecting the GPIO pins of the Raspberry Pi according to the GPIO.BOARD layout
cs_pin = 24
clock_pin = 23
data_pin = 22
units = "c"

thermocouple = MAX6675(cs_pin, clock_pin, data_pin, units)

def Return_temperature():
    return thermocouple.get()
    thermocouple.cleanup() # Careful with this. Not sure if this is required
    # or if it will mess up the GPIO setup for the Energenie board