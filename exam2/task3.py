dificult = int(input())
zavurtqnost = int(input())
pages = int(input())

if dificult >= 80 and zavurtqnost >= 80 and pages >=8:
    print("Legacy")
elif dificult >= 80 and zavurtqnost <= 10:
    print("Master")
elif zavurtqnost >= 50 and pages >= 2:
    print("Hard")
elif dificult > 30:
    print("Regular")
elif dificult <= 30 and pages <= 1:
    print("Easy")
elif dificult <= 10:
    print("Elementary")