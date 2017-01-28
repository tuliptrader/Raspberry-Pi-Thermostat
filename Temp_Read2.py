#Read the temperature from a DS18B20 Thermometer

#from w1thermsensor.w1thermsensor import W1ThermSensor

#import re

#sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "0416606a3cff")
#temperature_in_celsius = sensor.get_temperature()


#Temperature_Data = open("/sys/bus/w1/devices/28-0416606a3cff/w1_slave","r")

with open('/sys/bus/w1/devices/28-0416606a3cff/w1_slave', 'r') as content_file:
Temperature_Data = content_file.read()
print str(Temperature_Data)
print Temperature_Data