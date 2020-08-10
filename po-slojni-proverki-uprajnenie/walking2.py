steps = input()
all_steps = 0

while all_steps < 10000:
    all_steps += int(steps)
    if all_steps >= 10000:
        print(f"Goal reached! Good job!")
        break
    steps = input()

    while steps == "Going home":
        last_steps = int(input())
        all_steps += last_steps
        end_steps = 10000 - all_steps
        if all_steps > 10000:
            print(f"Goal reached! Good job!")
        else:
            print(f"{end_steps} more steps to reach goal.")


