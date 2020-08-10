number1 = int(input())
number2 = int(input())
sign = input()

if sign == "+":
    if (number1 + number2 ) % 2 == 0:
        print(f"{number1} + {number2} = {number1+number2} - even")
    else:
        print(f"{number1} + {number2} = {number1 + number2} - odd")

if sign == "-":
    if (number1 - number2 ) % 2 == 0:
        print(f"{number1} - {number2} = {number1-number2} - even")
    else:
        print(f"{number1} - {number2} = {number1 - number2} - odd")

if sign == "*":
    if (number1 * number2 ) % 2 == 0:
        print(f"{number1} * {number2} = {number1*number2} - even")
    else:
        print(f"{number1} * {number2} = {number1 * number2} - odd")

if sign == "/" and number2 != 0:
        print(f"{number1} / {number2} = {number1/number2:.2f}")

if sign == "%" and number2 != 0:
        print(f"{number1} % {number2} = {number1 % number2}")

if sign == "/" and number2 == 0:
        print(f"Cannot divide {number1} by zero")

if sign == "%" and number2 == 0:
    print(f"Cannot divide {number1} by zero")