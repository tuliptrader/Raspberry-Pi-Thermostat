from max6675 import MAX6675, MAX6675Error
from time import sleep

cs_pin = 24
clock_pin = 23
data_pin = 22
units = "c"

while True:
    thermocouple = MAX6675(cs_pin, clock_pin, data_pin, units)
    print(thermocouple.get())
    thermocouple.cleanup()
    sleep(10)
