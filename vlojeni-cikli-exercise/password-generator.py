n = int(input())
L = int(input())

for l1 in range(1, n):
    for l2 in range(1,n):
        for l3 in range(97, L + 97):
            for l4 in range(97, L + 97):
                for l5 in range(1, n + 1):
                    if l5 > l1 and l5 > l2:
                        print(f"{l1}{l2}{chr(l3)}{chr(l4)}{l5}", end = " ")