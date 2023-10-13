times = input('Enter time taken of 2 laps separated by semi-colon (seconds):' )

times_list = times.split(';')

firstlap_time = times_list[0] 
secondlap_time = times_list[1] 

if firstlap_time > secondlap_time: 
 best = firstlap_time 
else:
 best = secondlap_time 

total = firstlap_time + secondlap_time 

print("Tom's best time is {0} s and average time is {1} s".format(best,total/2))

