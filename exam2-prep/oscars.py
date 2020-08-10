actor_name = input()
initial_points = float(input())
number_of_asses = int(input())
all_points_from_one_ass = 0

for i in range(number_of_asses):
    asses_name = input()
    asses_points = float(input())
    initial_points = initial_points + ((len(asses_name) * asses_points) / 2)
    dif = abs(1250.5 - initial_points)

    if initial_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {initial_points:.1f}!")
        break

if initial_points < 1250.5:
    print(f"Sorry, {actor_name} you need {dif:.1f} more!")