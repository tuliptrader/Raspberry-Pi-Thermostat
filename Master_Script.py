# The file that runs the Thermostat code by importing other functions and bits of code into it

from time import sleep
import Temp_Read

#The code for

"""Monday_living = (insert schedule here
Tuesday_living = (insert other schedule here

Schedule_living = (Monday_living, Tuesday_living, etc. """

target_temp_living = 5

while True: #have script running continously
    try:
        if Temp_Read.Return_temperature()<= target_temp_living:
            # Turn on heating in living room, repeat once or twice
            # call function from Energenie Control.py


        else:
            #turn off heating in living room
            # call function from Energenie Control.py

        sleep(60) # sleep for 10 minutes perhaps? to avoid turning the heating on and off continuously

