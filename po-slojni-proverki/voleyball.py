import math

year = input()
holidays = int(input())
weekends = int(input())


all_weekends_play = (48 - weekends)  * (3/4)
weekend_plays = weekends * 1
holiday_plays = holidays *  (2/3)

all_plays = all_weekends_play + weekend_plays + holiday_plays

if year == "leap":
    all_plays *= 1.15
    print(math.floor(all_plays))
if year == "normal":
    print(math.floor(all_plays))