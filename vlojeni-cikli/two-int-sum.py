num1 = int(input())
num2 = int(input())
num3 = int(input())
count = 0
found = True

for i in range(num1, num2+1):
    for b in range(num1, num2+1):
        count += 1
        sum = i + b
        if sum == num3:
            found = False
            print(f"Combination N:{count} ({i} + {b} = {num3})")
            break
    if sum == num3:
        break

if found:
    print(f"{count} combinations - neither equals {num3}")
