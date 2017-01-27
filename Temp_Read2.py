#Read the temperature from a DS18B20 Thermometer

from w1thermsensor import W1ThermSensor


sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "0416606a3cff")
temperature_in_celsius = sensor.get_temperature()