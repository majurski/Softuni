degrees = int(input())
daytime = input()

outfit = ""
shoes = ""

if daytime == "Morning":
    if 10 <= degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    if 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    if degrees >= 25:
        outfit = "T-shirt"
        shoes = "Sandals"
elif daytime == "Afternoon":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    if 18 < degrees <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    if degrees >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"

elif daytime == "Evening":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    if 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    if degrees >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")