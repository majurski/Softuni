number = 4
b = "#","*","*","*",
red = []

for i in range(number):
    for c in b:
        red.append(c)

for u in range(number):
    print(*red[number+u:], sep = " ")
       