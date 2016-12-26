from max31855.max6675 import MAX6675, MAX6675Error

from datetime import datetime

cs_pin = 24
clock_pin = 23
data_pin = 22
units = "c"

log_interval = 5

while True:
    datafile = open("temperature_data_py.csv", "a")
    thermocouple = MAX6675(cs_pin, clock_pin, data_pin, units)
    temperature_now=thermocouple.get()

    info_now =str( datetime.now()+"; "+str(temperature_now))
    datafile.write(info_now)

    print(info_now)
    datafile.close()
    thermocouple.cleanup()
    sleep(log_interval)