coins = float(input())
act = round(coins * 100)
number = 0

while act > 0:
    if act >= 200:
        number += 1
        act -= 200
    elif act >= 100:
        number += 1
        act -= 100
    elif act >= 50:
        number += 1
        act -= 50
    elif act >= 20:
        number += 1
        act -= 20
    elif act >= 10:
        number += 1
        act -= 10
    elif act >= 5:
        number += 1
        act -= 5
    elif act >= 2:
        number += 1
        act -= 2
    elif act >= 1:
        number += 1
        act -= 1
        break

print(number)
