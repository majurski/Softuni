needed_money = float(input())
current_money = float(input())
days_counter = 0
spending_counter = 0

while current_money < needed_money and spending_counter < 5:
    type = input()
    money = float(input())
    days_counter += 1
    if type == "save":
        spending_counter = 0
        current_money += money
    elif type == "spend":
        spending_counter = 0
        current_money -= money
        if current_money < 0:
            current_money = 0


if spending_counter == 5:
    print(f"You can't save the money.")
    print(days_counter)

if current_money >= needed_money:
    print(f"You saved the money for {days_counter} days.")