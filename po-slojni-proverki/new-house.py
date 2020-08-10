flower_type = input()
count_flowers = int(input())
budget = int(input())

price = 0

if flower_type == "Roses":
    price = 5
    if count_flowers > 80:
        price *= 0.90
elif flower_type == "Dahlias":
    price = 3.8
    if count_flowers > 90:
        price *= 0.85
elif flower_type == "Tulips":
    price = 2.8
    if count_flowers > 80:
        price *= 0.85
elif flower_type == "Narcissus":
    price = 3
    if count_flowers < 120:
        price += price * 0.15
elif flower_type == "Gladiolus":
    price = 2.5
    if count_flowers < 80:
        price += price * 0.20

total = price * count_flowers

if budget >= total:
    money_left = budget - total
    print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {money_left:.2f} leva left.")
else:
    money_needed = total - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")