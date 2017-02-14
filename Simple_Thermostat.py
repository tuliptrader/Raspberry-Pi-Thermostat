from Ten_minute_temp import Ten_Minute_Average2
from Energenie_Control import energenie_socket
from Temperature_schedule import Target_temperature



def Heat_or_no_heat():
    Target = Target_temperature()

    if Ten_Minute_Average2() < Target: #Turn on socket
        energenie_socket(1,True)

    elif Ten_Minute_Average2() >= Target: #Turn off socket
        energenie_socket(1,False)


Heat_or_no_heat()
