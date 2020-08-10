flow_type = input()
number_flow = int(input())
season = input()

amount = 0
all_honey = 0

if flow_type == "Sunflower":
    if season == "Spring":
        amount = 10
    elif season == "Summer":
        amount = 8
    elif season == "Autumn":
        amount = 12

if flow_type == "Daisy":
    if season == "Spring":
        amount = 12
    elif season == "Summer":
        amount = 8
    elif season == "Autumn":
        amount = 6

if flow_type == "Lavender":
    if season == "Spring":
        amount = 12
    elif season == "Summer":
        amount = 8
    elif season == "Autumn":
        amount = 6

if flow_type == "Mint":
    if season == "Spring":
        amount = 10
    elif season == "Summer":
        amount = 12
    elif season == "Autumn":
        amount = 6

if season == "Spring":
    if flow_type == "Daisy" or flow_type == "Mint":
        amount += amount*0.1
        all_honey = number_flow * amount

elif season == "Summer":
    all_honey = number_flow * amount
    all_honey += all_honey*0.1

elif season == "Autumn":
    all_honey = number_flow * amount
    all_honey -= all_honey*0.05

print(f"Total honey harvested: {all_honey:.2f}")