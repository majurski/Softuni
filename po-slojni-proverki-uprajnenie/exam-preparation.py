grades_number = int(input())
line = input()
count_tasks = 0
current_bad_grades = 0
total_grades = 0
task_name = ""

while line != "Enough":
    count_tasks += 1
    grades_number = int(input())
    task_name = input()
    grade = int(input())
    total_grades += grade
    if grade <= 4:
        current_bad_grades += 1
    if current_bad_grades >= grades_number:
        print(f"You need a break, {count_tasks} poor grades.")
        break
    line = input()

avr_score = total_grades / count_tasks

print(f"Average score: {avr_score}")
print(f"Number of problems: {count_tasks}")
print(f"Last problem: {task_name}")