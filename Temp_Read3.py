#Read the temperature from a DS18B20 Thermometer
from datetime import datetime
import re

for line in open('/sys/bus/w1/devices/28-0416606a3cff/w1_slave', 'r'):
	Temperature_Data = re.findall("t=\d{5}", line)

Living_Room = int(str(Temperature_Data)[4:8])/1000
print Living_Room

"""print content_file.read()

Data_string = content_file.read()

print Data_string

for i in Data_string:

	Temperature_Data = re.findall("t=\d{5}", i)
	print Temperature_Data

print Temperature_Data
# re.search('(?<=-)\w+', 'spam-egg')"""

#Living_Room = float(Temperature_Data) / 1000

print(str(Living_Room) + "Celsius using RegEx")

datafile = open("/home/pi/Python_Stuff/Thermostat_Data/Data3.csv", "a")

info_now = str(datetime.now()) + "; " + str(Living_Room) + "\n"

datafile.write(info_now)

print(info_now)
datafile.close()