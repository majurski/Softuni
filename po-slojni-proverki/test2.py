product = input()
day = input()
quantity = float(input())
price = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if product == "banana":
        price = 2.50
    elif product == "apple":
        price = 1.20
    elif product == "orange":
        price = 0.85
    elif product == "grapefruit":
        price = 1.45
    elif product == "kiwi":
        price = 2.70
    elif product == "pineapple":
        price = 5.50
    elif product == "grapes":
        price = 3.85
    elif product != "banana" or product != "apple" or product != "grapefruit" or product != "kiwi" or day != "pineapple" or day != "grapes":
        print("")
    result = quantity * price
    print(f"{result:.2f}")

elif day == "Saturday" or day == "Sunday":
    if product == "banana":
        price = 2.70
    elif product == "apple":
        price = 1.25
    elif product == "orange":
        price = 0.90
    elif product == "grapefruit":
        price = 1.60
    elif product == "kiwi":
        price = 3.00
    elif product == "pineapple":
        price = 5.60
    elif product == "grapes":
        price = 4.20
    elif product != "banana" or product != "apple" or product != "grapefruit" or product != "kiwi" or day != "pineapple" or day != "grapes":
        print("")
    result = quantity * price
    print(f"{result:.2f}")

elif day != "Monday" or day != "Tuesday" or day != "Wednesday" or day != "Thursday" or day != "Friday" or day != "Saturday" or day != "Sunday":
    print("error")
