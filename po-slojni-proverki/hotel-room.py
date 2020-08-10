month = input()
days = int(input())

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if days > 7 and days <=14:
        studio_price *= 0.95
    if days > 14:
        studio_price *= 0.70
        apartment_price *= 0.90

if month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if days > 14:
        studio_price *= 0.80
        apartment_price *= 0.90

if month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if days > 14:
        apartment_price *= 0.90

allholidayAp = apartment_price * days
allholidaySt = studio_price * days


print(f"Apartment: {allholidayAp:.2f} lv.")
print(f"Studio: {allholidaySt:.2f} lv.")