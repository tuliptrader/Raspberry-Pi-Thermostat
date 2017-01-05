import RPi.GPIO as GPIO
import time
import datetime

# Setting the Raspberry Pi up with the Energenie Control board to control the Energenie Sockets
# set the pins numbering mode
GPIO.setmode(GPIO.BOARD)

# Select the GPIO pins that the Energenie Control board is plugged into.
Pin_A = 11
Pin_B = 15
Pin_C = 16
Pin_D = 13
Pin_E = 18
Pin_F = 22

# Select the GPIO pins used for the encoder K0-K3 data inputs
GPIO.setup(Pin_A, GPIO.OUT)
GPIO.setup(Pin_B, GPIO.OUT)
GPIO.setup(Pin_C, GPIO.OUT)
GPIO.setup(Pin_D, GPIO.OUT)

# Select the signal to select ASK/FSK
GPIO.setup(Pin_E, GPIO.OUT)

# Select the signal used to enable/disable the modulator
GPIO.setup(Pin_F, GPIO.OUT)

# Disable the modulator by setting CE pin lo
GPIO.output (Pin_F, False)

# Set the modulator to ASK for On Off Keying
# by setting MODSEL pin lo
GPIO.output (Pin_E, False)

# Initialise K0-K3 inputs of the encoder to 0000
GPIO.output (Pin_A, False)
GPIO.output (Pin_B, False)
GPIO.output (Pin_C, False)
GPIO.output (Pin_D, False)

