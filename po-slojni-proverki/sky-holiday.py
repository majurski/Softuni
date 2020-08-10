days = int(input())
room_type = input()
rating = input()

nights = days - 1

price_per_night = 0
discount_percentage = 0

if days < 10:
    if room_type == "room for one person":
        price_per_night = 18.0
    elif room_type == "apartment":
        price_per_night = 25.0
        discount_percentage = 30
    else:
        price_per_night = 35
        discount_percentage = 15

elif 10 <= days <= 15:
    if room_type == "room for one person":
        price_per_night = 18.0
    elif room_type == "apartment":
        price_per_night = 25.0
        discount_percentage = 35
    else:
        price_per_night = 35
        discount_percentage = 15

else:
    if room_type == "room for one person":
        price_per_night = 18.0
    elif room_type == "apartment":
        price_per_night = 25.0
        discount_percentage = 50
    else:
        price_per_night = 35
        discount_percentage = 20

total_price = price_per_night * nights
discount = total_price * discount_percentage / 100

total_price = total_price - discount

if rating == "positive":
    total_price = total_price * 1.25
else:
    total_price = total_price * 0.9

print(f"{total_price:.2f}")
