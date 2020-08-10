number_students = int(input())
problems = int(input())
energy = int(input())
counter_problem_solved = 0
counter_ques = 0

while True:
    counter_problem_solved += problems
    energy += 2 * problems

    number_students -= 1 * problems
    energy -= number_students * 2 * 3
    counter_ques += number_students * 2

    if number_students < 10:
        print(f"The students are too few!")
        print(f"Problems solved: {counter_problem_solved}")
        break

    if number_students > 10 and energy > 0:
        number_students += number_students // 10

    if energy <= 0:
        print(f"The trainer is too tired!")
        print(f"Questions answered: {counter_ques}")
        break




