# Import the MPU6050 class from the MPU6050.py file
from MPU6050 import MPU6050
import glob, datetime, os, time
import time

log_period = 10 # seconds

# Create a new instance of the MPU6050 class
sensor = MPU6050(0x68)

# Obtain an initial time from which to generate timestamps
start = time.time()

# Clear and open the data file for writing
outfile = open("temperature_data_py.csv", "a")

# Create a listener function for changes in thermocouple temperature
def TemperatureDataHandler():
    global start
    global outfile

    now = time.time()- start

    # assign temperature measured by IMU6050 to a variable
    ambientTemp=sensor.get_temp()

    # Write the data to the text file
    outfile.write(str(now) + "," + str(ambientTemp) + "\n")

    time.sleep(log_period)
# Write a header to the text file first thing
outfile.write("Time,Thermocouple-Temperature,Ambient-Board-Temperature\n")

while True:
    TemperatureDataHandler()