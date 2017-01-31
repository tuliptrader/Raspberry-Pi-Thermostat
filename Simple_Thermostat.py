from Ten_minute_temp import Ten_Minute_Average2
from Energenie_Control import energenie_socket

def Heat_or_no_heat():
    if Ten_Minute_Average2() < 16: #Turn on socket
        energenie_socket(1,True)

    elif Ten_Minute_Average2() >= 16: #Turn off socket
        energenie_socket(1,False)


Heat_or_no_heat()
