N = int(input())

for i in range(1111,9000):
    new = str(i)
    if new[1] != "0" and new[2] != "0" and new[3] != "0":
        if N % int(new[0]) == 0 and N % int(new[1]) == 0 and N % int(new[2]) == 0 and N % int(new[3]) == 0:
            print(i, end = " ")