budget = float(input())
season = input()

type_holiday = ""
destination = ""

price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = 0.30 * budget
    else:
        price = 0.70 * budget
elif budget <=1000:
    destination = "Balkans"
    if season == "summer":
        price = 0.40 * budget
    else:
        price = 0.80 * budget
elif budget > 1000:
    destination = "Europe"
    price = 0.9 * budget

if season == "summer" and destination != "Europe":
    type_holiday = "Camp"
else:
    type_holiday = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_holiday} - {price:.2f}")