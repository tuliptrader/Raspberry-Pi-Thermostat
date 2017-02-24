from Ten_minute_temp import Ten_Minute_Average2
from Energenie_Control import energenie_socket
from Temperature_schedule import Target_temperature
import RPi.GPIO as GPIO

print "I am printing from the impoort in Simple_Thermostat"
def Thermostat():
    Target = Target_temperature()

    if Ten_Minute_Average2() < Target: #Turn on socket

        energenie_socket(1,True)
        #GPIO.cleanup()
        print "I am printing from the decision thing"

    else: #Ten_Minute_Average2() >= Target: #Turn off socket

        energenie_socket(1,False)
        #GPIO.cleanup()


Thermostat()
GPIO.cleanup()