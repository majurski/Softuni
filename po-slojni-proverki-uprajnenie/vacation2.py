goal = float(input())
budget = float(input())
count_days = 0
count_spending_days = 0

while budget < goal and count_spending_days < 5:
    command = input()
    count_days += 1
    if command == "spend":
        amount = float(input())
        count_spending_days += 1
        budget -= amount
        if budget < 0:
            budget = 0
    else:
        amount = float(input())
        count_spending_days = 0
        budget += amount

if count_spending_days == 5:
    print(f"You can't save the money.")
    print(count_days)

if budget >= goal:
    print(f"You saved the money for {count_days} days.")
