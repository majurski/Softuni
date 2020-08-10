student_name = input()
bigger = True
while student_name != "Midnight":
    all_points = 0
    for i in range(6):
        points = int(input())
        all_points += points
        if points < 0:
            print(f"{student_name} was cheating!")
            bigger = False
            break
    equal = all_points / 600 * 100
    equal = round(equal)
    end_result = equal * 0.06

    if end_result < 5 and bigger == True:
        if end_result < 3:
            print(f"{student_name} - 2.00")
        else:
            print(f"{student_name} - {end_result:.2f}")
    if end_result >= 5:
        print(f"===================")
        print(f"|   CERTIFICATE   |")
        print(f"|    {end_result:.2f}/6.00    |")
        print(f"===================")
        print(f"Issued to {student_name}")
    if student_name == "Midnight":
        break

    student_name = input()