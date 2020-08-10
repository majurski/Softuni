steps = 0
sum_steps = 0
command = input()

while sum_steps < 10000:
    if command != "Going home":
        steps = int(command)
        sum_steps += steps
    else:
        steps = int(input())
        sum_steps += steps
        break
    command = input()

if sum_steps < 10000:
    print(f'{10000 - sum_steps} more steps to reach goal.')
else:
    print('Goal reached! Good job!')