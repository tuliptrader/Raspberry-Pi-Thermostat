#Read the temperature from a DS18B20 Thermometer
from datetime import datetime
import re

content_file = open('/sys/bus/w1/devices/28-0416606a3cff/w1_slave', 'r')

Temperature_Data = re.search("(?<=t=).....", content_file)

#re.search('(?<=-)\w+', 'spam-egg')

Living_Room = float(Temperature_Data) / 1000

print(str(Living_Room) + "Celsius using RegEx")

datafile = open("/home/pi/Python_Stuff/Thermostat_Data/Data3.csv", "a")

info_now = str(datetime.now()) + "; " + str(Living_Room) + "\n"

datafile.write(info_now)

print(info_now)
datafile.close()