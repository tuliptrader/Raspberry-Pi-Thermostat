from Energenie_Control import energenie_socket
import RPi.GPIO as GPIO

try:
    while True:
        raw_input('hit return key to send socket 1 ON code')
        energenie_socket(1,True)

        raw_input('hit return key to send socket 1 ON code')
        energenie_socket(1,False)

# Clean up the GPIOs for next time
except KeyboardInterrupt:
	GPIO.cleanup()