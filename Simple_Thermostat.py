from Ten_minute_temp import Ten_Minute_Average2
from Energenie_Control import energenie_socket
from Temperature_schedule import Target_temperature
import RPi.GPIO as GPIO


def Thermostat():
    Target = Target_temperature()

    if Ten_Minute_Average2() < Target: #Turn on socket
        #GPIO.cleanup()
        energenie_socket(1,True)

    else: #Ten_Minute_Average2() >= Target: #Turn off socket
        #GPIO.cleanup()
        energenie_socket(1,False)


Thermostat()