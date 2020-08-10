exam_hour = int(input())
exam_min = int(input())
arive_hour = int(input())
arive_min = int(input())

all_minutes_exam = exam_hour * 60 + exam_min
all_minutes_arive = arive_hour * 60 + arive_min

diference = 0

if all_minutes_exam == all_minutes_arive:
    case = 0
if all_minutes_exam > all_minutes_arive:
    diference = all_minutes_exam - all_minutes_arive
    if diference > 0 and diference <= 30:
        case = 1
    if diference > 30 and diference < 60:
        case = 2
    if diference >= 60:
        case = 3
if all_minutes_exam < all_minutes_arive:
    diference = all_minutes_arive - all_minutes_exam
    if diference > 0 and diference <= 30:
        case = 4
    if diference > 30:
        case = 5
    if diference >= 60:
        case = 6

if case == 0 or case == 1:
    print("On time")
if case == 2 or case == 3 :
    print("Early")
if case == 4 or case == 5 or case == 6:
    print("Late")

new_time_h = diference // 60
new_time_m = diference % 60

if case == 1 or case == 2:
    print(f"{new_time_m} minutes before the start")
if case == 3:
    if new_time_m < 10:
        print(f"{new_time_h}:0{new_time_m} hours before the start")
    else:
        print(f"{new_time_h}:{new_time_m} hours before the start")
if case == 4 or case == 5:
    print(f"{new_time_m} minutes after the start")
if case == 6:
    if new_time_m < 10:
        print(f"{new_time_h}:0{new_time_m} hours after the start")
    else:
        print(f"{new_time_h}:{new_time_m} hours after the start")
