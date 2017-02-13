from  datetime import datetime
import calendar

def Target_temperature():
	my_date = datetime.now() # assign the date object to the variable my_date
	The_weekday = calendar.day_name[my_date.weekday()] #find the day of the week object, and find out what this is as a written day
	#print Weekday

	The_hour = my_date.hour
	The_minute = my_date.minute
	#print my_date.hour
	#print my_date.minute

	my_str =  str(The_weekday) + ',' + str(The_hour) +':' + str(The_minute)[0]
	#my_str = "Monday,02:1"
	#print my_str

	#my_regex = the string that I will be searching for in the Schedule.csv file

	for line in open('Schedule_livingroom.csv','r'):
		if my_str in line:
			Info = line

	#print Info

	Target = Info[-3:-1]

	return Target
	print Target

print Target_temperature()
