#File to test Energenie_Control
from time import sleep
import Energenie_Control

while True:
    Energenie_Control(1,True)
    sleep(5)
    Energenie_Control(1,False)
    sleep(5)