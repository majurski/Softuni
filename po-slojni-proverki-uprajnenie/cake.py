width = int(input())
height = int(input())

area = width * height

line = input()

while line != "STOP":
    count_pieces = int(line)
    area -= count_pieces
    if area < 0:
        print(f"No more cake left! You need {abs(area)} pieces more.")
        break

    line = input()

if line == "STOP":
    print(f"{area} pieces are left.")