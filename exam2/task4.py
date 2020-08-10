import math
number_students = int(input())
seasons = int(input())

for i in range(1, seasons+1):
    for b in range(2):
        number_students -= number_students - math.ceil(number_students * 0.9)
    number_students -= number_students - math.ceil(number_students * 0.8)
    if i % 3 == 0:
        number_students += math.ceil(number_students * 0.15)
    else:
        number_students += math.ceil(number_students * 0.05)





print(f"Students: {number_students}")