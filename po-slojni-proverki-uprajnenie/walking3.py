goal = 10000
step_counter = 0
home_steps = 0

while step_counter < goal:
    line = input()
    if line == "Going home":
        home_steps = int(input())
        step_counter += home_steps
        break
    line = int(line)
    step_counter += line

if step_counter < goal:
    print(f'{abs(goal - step_counter)} more steps to reach goal.')
else:
    print(f'Goal reached! Good job!')