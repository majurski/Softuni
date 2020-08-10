number_bees = int(input())
health = int(input())
atack = int(input())

while True:
    number_bees -= atack
    health -= number_bees * 5
    if number_bees < 0:
        break
    if number_bees < 100:
        print(f"The bear stole the honey! Bees left {number_bees}.")
        break
    elif health < 0:
        print(f"Beehive won! Bees left {number_bees}.")
        break
    else:
        print(f"The bear stole the honey! Bees left {number_bees}.")
        break