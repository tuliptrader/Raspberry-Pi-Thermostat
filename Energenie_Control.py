# Code to turn Energenie sockets on and off

#import the required modules
import RPi.GPIO as GPIO
import time
print "I am running!!!! in Energenie_Control"
# set the pins numbering mode

GPIO.setmode(GPIO.BOARD)

# Select the GPIO pins used for the encoder K0-K3 data inputs
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# Select the signal to select ASK/FSK
GPIO.setup(18, GPIO.OUT)

# Select the signal used to enable/disable the modulator
GPIO.setup(22, GPIO.OUT)

# Disable the modulator by setting CE pin lo
GPIO.output (22, False)

# Set the modulator to ASK for On Off Keying
# by setting MODSEL pin lo
GPIO.output (18, False)

# Initialise K0-K3 inputs of the encoder to 0000
GPIO.output (11, False)
GPIO.output (15, False)
GPIO.output (16, False)
GPIO.output (13, False)

def energenie_socket(socket, state): # sockets (1,2,3,4,all) and state (True, False)
	# We will just loop round switching the units on and off

    if socket == 1:
        if state == True:
            # Set K0-K3
            #print "sending code 1111 socket 1 on"
            GPIO.output (11, True)
            GPIO.output (15, True)
            GPIO.output (16, True)
            GPIO.output (13, True)
            # let it settle, encoder requires this
            time.sleep(0.1)
            # Enable the modulator
            GPIO.output (22, True)
            # keep enabled for a period
            time.sleep(0.25)
            # Disable the modulator
            GPIO.output (22, False)

        elif state == False:
            # Set K0-K3
            #print "sending code 0111 Socket 1 off"
            GPIO.output (11, True)
            GPIO.output (15, True)
            GPIO.output (16, True)
            GPIO.output (13, False)
            # let it settle, encoder requires this
            time.sleep(0.1)
            # Enable the modulator
            GPIO.output (22, True)
            # keep enabled for a period
            time.sleep(0.25)
            # Disable the modulator
            GPIO.output (22, False)

    elif socket == 2:
        if state == True:
            # Set K0-K3
            #print "sending code 1110 socket 2 on"
            GPIO.output (11, False)
            GPIO.output (15, True)
            GPIO.output (16, True)
            GPIO.output (13, True)
            # let it settle, encoder requires this
            time.sleep(0.1)
            # Enable the modulator
            GPIO.output (22, True)
            # keep enabled for a period
            time.sleep(0.25)
            # Disable the modulator
            GPIO.output (22, False)

        elif state == False:
            # Set K0-K3
            #print "sending code 0110 socket 2 off"
            GPIO.output (11, False)
            GPIO.output (15, True)
            GPIO.output (16, True)
            GPIO.output (13, False)
            # let it settle, encoder requires this
            time.sleep(0.1)
            # Enable the modulator
            GPIO.output (22, True)
            # keep enabled for a period
            time.sleep(0.25)
            # Disable the modulator
            GPIO.output (22, False)

    elif socket == 3:
    	if state is True:
            GPIO.output (11, True)
            GPIO.output (15, False)
            GPIO.output (16, True)
            GPIO.output (13, True)
            # let it settle, encoder requires this
            time.sleep(0.1)
            # Enable the modulator
            GPIO.output (22, True)
            # keep enabled for a period
            time.sleep(0.25)
            GPIO.output(22, False)

        elif state == False:
            # Set K0-K3
            #print "sending code 0101 socket 3 off"
            GPIO.output (11, True)
            GPIO.output (15, False)
            GPIO.output (16, True)
            GPIO.output (13, False)
            # let it settle, encoder requires this
            time.sleep(0.1)
            # Enable the modulator
            GPIO.output (22, True)
            # keep enabled for a period
            time.sleep(0.25)
            # Disable the modulator
            GPIO.output (22, False)

	"""elif socket == 4:
        if state == True:
            GPIO.output(13, True)
            # Set K0-K3
            #print "sending code 1100 socket 4 on"
            # GPIO.output (11, False)
            # GPIO.output (15, False)
            # GPIO.output (16, True)

            # let it settle, encoder requires this
            time.sleep(0.1)
            # Enable the modulator
            GPIO.output (22, True)
            # keep enabled for a period
            # time.sleep(0.25)
            #  Disable the modulator
            # GPIO.output (22, False)

        elif state == False:
            # Set K0-K3
            print "sending code 0100 socket 4 off"
            GPIO.output (11, False)
            GPIO.output (15, False)
            GPIO.output (16, True)
            GPIO.output (13, False)
            # let it settle, encoder requires this
            time.sleep(0.1)
            # Enable the modulator
            GPIO.output (22, True)
            # keep enabled for a period
            time.sleep(0.25)
            # Disable the modulator
            GPIO.output (22, False)

    elif socket == all:
         if state == True:
		# Set K0-K3
            #print "sending code 1011 ALL on"
            GPIO.output (11, True)
            GPIO.output (15, True)
            GPIO.output (16, False)
            GPIO.output (13, True)
            # let it settle, encoder requires this
            time.sleep(0.1)
            # Enable the modulator
            GPIO.output (22, True)
            # keep enabled for a period
            time.sleep(0.25)
            # Disable the modulator
            GPIO.output (22, False)

         elif state == False:
            # Set K0-K3
            #print "sending code 0011 All off"
            GPIO.output (11, True)
            GPIO.output (15, True)
            GPIO.output (16, False)
            GPIO.output (13, False)
            # let it settle, encoder requires this
            time.sleep(0.1)
            # Enable the modulator
            GPIO.output (22, True)
            # keep enabled for a period
            time.sleep(0.25)
            # Disable the modulator
            GPIO.output (22, False)
    """

    GPIO.cleanup()
    # Clean up the GPIOs for next time
    except KeyboardInterrupt:
        GPIO.cleanup()