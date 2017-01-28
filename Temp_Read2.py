#Read the temperature from a DS18B20 Thermometer
from datetime import datetime

with open('/sys/bus/w1/devices/28-0416606a3cff/w1_slave', 'r') as content_file:
    Temperature_Data = content_file.read()
    #print(Temperature_Data)

    variable = Temperature_Data[-6:]

    Living_Room = float(variable) / 1000

    #print(str(Living_Room) + "Celsius")

    datafile = open("/home/pi/Python_Stuff/Thermostat_Data/Data.csv", "a")

    info_now = str(datetime.now()) + "; " + str(Living_Room) + "\n"

    datafile.write(info_now)

    print(info_now)
    datafile.close()