level = int(input())
rooms = int(input())

for l in range(level, 0, -1):
    for r in range(rooms):
        if l == level:
            print(f"L{l}{r} ", end = "")
        elif l % 2 == 0:
            print(f"O{l}{r} ", end = "")
        else:
            print(f"A{l}{r} ", end = "")

    print()