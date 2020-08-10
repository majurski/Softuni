N = int(input())

for i in range(1111,10000):
    for b in range(0, 4):
        digit = str(i)[b]
        new_int = int(digit)
        work = False
        if N >= new_int and new_int != 0:
            if N % new_int == 0:
                work = True
    if work:
        print(i, end = " ")
