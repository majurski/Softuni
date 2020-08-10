red = int(input())

width = red
height = width + width / 2
height = int(height)

cash = []
for i in range(height):
    for b in range(width):
        if (i + b) % 4 == 0:
            cash.append("#")
        else:
            cash.append(".")

for i in range(0, len(cash), width):
    print(*cash[i:i+width], sep='')