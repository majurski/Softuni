exam_hour = int(input())
exam_min = int(input())
arive_hour = int(input())
arive_min = int(input())

all_minutes_exam = exam_hour * 60 + exam_min
all_minutes_arive = arive_hour * 60 + arive_min

info = 0
diference = 0

if all_minutes_exam > all_minutes_arive:
    diference = all_minutes_exam - all_minutes_arive
    info = 1
    if diference > 30:
        info = 31
if all_minutes_exam < all_minutes_arive:
    diference = all_minutes_arive - all_minutes_exam
    info = -1

new_time_h = diference // 60
new_time_m = diference % 60


if info >= 0:
    if info == 0:
        print("On time")
    elif info < 30 and info != 0:
        print("On time")
        if new_time_m < 10:
            if new_time_h == 0:
                print(f"{new_time_m} minutes  before the start")
            else:
                print(f"{new_time_h} hours :0{new_time_m} minutes  before the start")
        else:
            if new_time_h == 0:
                print(f"{new_time_m} minutes before the start")
            else:
                print(f"{new_time_h} hours :{new_time_m} minutes before the start")
    else:
        print("Early")
        if new_time_m < 10:
            if new_time_h == 0:
                print(f"{new_time_m} minutes before the start")
            else:
                print(f"{new_time_h} hours :0{new_time_m} minutes before the start")
        else:
            if new_time_h == 0:
                print(f"{new_time_m} minutes before the start")
            else:
                print(f"{new_time_h} hours :{new_time_m} minutes before the start")
if info < 0:
    print("Late")
    if new_time_h == 0:
        print(f"{new_time_m} minutes after the start")
    else:
        print(f"{new_time_h}:{new_time_m} minutes after the start")