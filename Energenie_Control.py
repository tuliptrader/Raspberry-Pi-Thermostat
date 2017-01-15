# Code to turn Energenie sockets on and off



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

        if state == False:
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

    if socket == 2:
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

        if State == False
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
    if socket == 3:
		if state == True:
            # Set K0-K3
            #print "sending code 1101 socket 3 on"
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
            # Disable the modulator
            GPIO.output (22, False)

		if state == False:
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

	if socket == 4:
        if state == True:
            # Set K0-K3
            #print "sending code 1100 socket 4 on"
            GPIO.output (11, False)
            GPIO.output (15, False)
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

		if state == False:
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

    if socket == all:
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

        if state == False:
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

# Clean up the GPIOs for next time
except KeyboardInterrupt:
	GPIO.cleanup()
