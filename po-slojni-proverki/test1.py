product = input()
day = input()
quantity = float(input())
price = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if product == "banana":
        price = 2.50
        result = quantity * price
        print(f"{result:.2f}")
    elif product == "apple":
        price = 1.20
        result = quantity * price
        print(f"{result:.2f}")
    elif product == "orange":
        price = 0.85
        result = quantity * price
        print(f"{result:.2f}")
    elif product == "grapefruit":
        price = 1.45
        result = quantity * price
        print(f"{result:.2f}")
    elif product == "kiwi":
        price = 2.70
        result = quantity * price
        print(f"{result:.2f}")
    elif product == "pineapple":
        price = 5.50
        result = quantity * price
        print(f"{result:.2f}")
    elif product == "grapes":
        price = 3.85
        result = quantity * price
        print(f"{result:.2f}")
    else:
        print("error")

elif day == "Saturday" or day == "Sunday":
    result = quantity * price
    if product == "banana":
        price = 2.70
        result = quantity * price
        print(f"{result:.2f}")
    elif product == "apple":
        price = 1.25
        result = quantity * price
        print(f"{result:.2f}")
    elif product == "orange":
        price = 0.90
        result = quantity * price
        print(f"{result:.2f}")
    elif product == "grapefruit":
        price = 1.60
        result = quantity * price
        print(f"{result:.2f}")
    elif product == "kiwi":
        price = 3.00
        result = quantity * price
        print(f"{result:.2f}")
    elif product == "pineapple":
        price = 5.60
        result = quantity * price
        print(f"{result:.2f}")
    elif product == "grapes":
        price = 4.20
        result = quantity * price
        print(f"{result:.2f}")
    else:
        print("error")
else:
    print("error")

