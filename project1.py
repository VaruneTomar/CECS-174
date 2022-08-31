#Varune Tomar

#Asking the user to enter the current time 
time_now = int(input("Enter the current time now in hours: "))

#asking the user the number of hours to wait for the alarm
wait_time = int(input("Enter the number of hours to wait for the alarm: "))

#adding the current time with the wait time
total_hours = time_now + wait_time

#using the modulus operator to find the final time
if total_hours == 24:
    final_alarm_time = 24
else:
    final_alarm_time = total_hours % 24

#convert military time to standard time
standardtime = final_alarm_time - 12

#using if else statemenets to determine am or pm
if final_alarm_time == 24:
    print(final_alarm_time,',',standardtime,":00 AM")
elif final_alarm_time < 12:
    print(final_alarm_time,',',final_alarm_time,":00 AM")
elif final_alarm_time == 12:
    print(final_alarm_time,',',final_alarm_time,":00 PM",sep='')
elif final_alarm_time > 12:
    print(final_alarm_time,',',standardtime,":00 PM")
     
    

    
