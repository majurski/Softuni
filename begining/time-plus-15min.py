
#hours = int(input())
#minutes = int(input())

hours = 23
minutes = 55

total = hours * 60 + minutes + 15

finelh = total // 60
finelm = total % 60

if finelh > 23:
	finelh -= 24


if finelm < 10:
	print(f"{finelh}:0{finelm}")
else:
	print(f"{finelh}:{finelm}")

