#Read the temperature from a DS18B20 Thermometer

#with open('/sys/bus/w1/devices/28-0416606a3cff/w1_slave', 'r') as content_file:
#    Temperature_Data = content_file.read()
 #   print Temperature_Data
#
 #   variable = Temperature_Data[-6:]
#
 #   Living_Room = float(variable) / 1000
#
 ##   print Living_Room

content_file = open('/sys/bus/w1/devices/28-0416606a3cff/w1_slave', 'r')

Temperature_Data = content_file.read()
print   Temperature_Data
variablex =Temperature_Data[-6:]

Living_room = float(variablex)/1000
return Living_room