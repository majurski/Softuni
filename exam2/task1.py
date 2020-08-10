import math

number_students = int(input())
number_task = int(input())

sended = number_students * math.ceil(number_task * 2.8)


aditional = number_students * round(number_task / 3)
all = sended + aditional

needed = 5 * math.ceil(all / 10)

print(f"{needed} KB needed")
print(f"{all} submissions")