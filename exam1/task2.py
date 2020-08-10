intelkt = int(input())
power = int(input())
gender = input()


if intelkt >= 80:
    if power >= 80:
        if gender == "female":
            print("Queen Bee")

    elif power < 80:
        if gender == "female" or gender == "male":
            print("Repairing Bee")

elif intelkt >= 60:
    print("Cleaning Bee")

elif power >= 80:
    print("Drone Bee")

elif power >= 60:
    print("Guard Bee")

else:
    print("Worker Bee")


