import math

time1 = 59
time2 = 59
time3 = 59
#time1 = int(input())
#time2 = int(input())
#time3 = int(input())

totaltime = time1 + time2 + time3

minutes = totaltime / 60
seconds = totaltime % 60
print(minutes)
print(seconds)
minutes = math.floor(minutes)
print(minutes)
if seconds < 10:
	print(f"{minutes}:0{seconds}")
else:
	print(f"{minutes}:{seconds}")