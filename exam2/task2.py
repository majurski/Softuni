number_task = int(input())
points = int(input())
course = input()

all_points = 0

if number_task == 1:
    if course == "Basics" and points != 0:
        all_points = 8 * points / 100
    elif course == "Fundamentals" and points != 0:
        all_points = 11 * points / 100
    elif course == "Advanced" and points != 0:
        all_points = 14 * points / 100

elif number_task == 2:
    if course == "Basics" and points != 0:
        all_points = 9 * points / 100
    elif course == "Fundamentals" and points != 0:
        all_points = 11 * points / 100
    elif course == "Advanced" and points != 0:
        all_points = 14 * points / 100

elif number_task == 3:
    if course == "Basics" and points != 0:
        all_points = 9 * points / 100
    elif course == "Fundamentals" and points != 0:
        all_points = 12 * points / 100
    elif course == "Advanced" and points != 0:
        all_points = 15 * points / 100

elif number_task == 4:
    if course == "Basics" and points != 0:
        all_points = 10 * points / 100
    elif course == "Fundamentals" and points != 0:
        all_points = 13 * points / 100
    elif course == "Advanced" and points != 0:
        all_points = 16 * points / 100

if course == "Advanced" and points != 0:
    all_points += all_points * 0.2
if course == "Basics" and points != 0:
    all_points -= all_points * 0.2

if points != 0:
    print(f"Total points: {all_points:.2f}")