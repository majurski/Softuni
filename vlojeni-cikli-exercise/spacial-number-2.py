N = int(input())

for i in range(1111,10000):
    work = False
    new = str(i)
    if new[0] != "0" and new[1] != "0" and new[2] != "0" and new[3] != "0":
        if N % int(new[0]) == 0 and N % int(new[1]) == 0 and N % int(new[2]) == 0 and N % int(new[3]) == 0:
            work = True
    if work:
        print(i, end = " ")