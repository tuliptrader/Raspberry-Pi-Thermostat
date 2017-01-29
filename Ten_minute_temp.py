#from itertools import islice

"""def Ten_Minute_Average():
    with open("datafile") as myfile:
        tail = list(islice(myfile, N))

        print tail"""



def Ten_Minute_Average2():
    file_x = open('/home/pi/Python_Stuff/Thermostat_Data/Data.csv')
    #print(file_x)
    last_ten_lines = list(file_x)[-10:]
    #last_ten_one = last_ten_lines[1]

    #print(last_ten_lines)
    #print(last_ten_one)
    #print(last_ten_one[28:])

    total = float(0)
    for x in range(0,10,1):
        #print x
        k = last_ten_lines[x]
        variable = k[28:]
        total = total + float(variable)

    temp_last_ten = float(total) /10

    return  temp_last_ten
    print temp_last_ten
    file_x.close()

Ten_Minute_Average2()