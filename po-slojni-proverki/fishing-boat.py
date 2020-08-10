budget = int(input())
season = input()
count_fishers = int(input())


if season == "Spring":
    price = 3000

elif season == "Summer" or season == "Autumn":
    price = 4200

elif season == "Winter":
    price = 2600


if count_fishers <= 6:
    price *= 0.90
if 7 <= count_fishers <= 11:
    price *= 0.85
if count_fishers >= 12:
    price *= 0.75

if count_fishers % 2 == 0 and season != "Autumn":
    price *= 0.95

if price <= budget:
    money_left = budget - price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")

