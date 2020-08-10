steps = input()
all_steps = 0
last_steps = 0

while steps != "Going home":
    all_steps += int(steps)
    if all_steps >= 10000:
        print(f"Goal reached! Good job!")
        break
    steps = input()


    if steps == "Going home":
        steps = input()
        last_steps = int(steps)
        all_steps += last_steps
        end_steps = 10000 - all_steps
        if all_steps > 10000:
            print(f"Goal reached! Good job!")
        else:
            print(f"{end_steps} more steps to reach goal.")
        break


