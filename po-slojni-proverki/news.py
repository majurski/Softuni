town = input()
sales = float(input())

comossion_percentage = 0

if 0 <= sales <= 500:
    if town == "Sofia":
        comossion_percentage = 5
    elif town == "Varna":
        comossion_percentage = 4.5
    elif town == "Plovdiv":
        comossion_percentage = 5.5

elif 500 < sales <= 1000:
    if town == "Sofia":
        comossion_percentage = 7
    elif town == "Varna":
        comossion_percentage = 7.5
    elif town == "Plovdiv":
        comossion_percentage = 8

elif 1000 < sales <= 10000:
    if town == "Sofia":
        comossion_percentage = 8
    elif town == "Varna":
        comossion_percentage = 10
    elif town == "Plovdiv":
        comossion_percentage = 12

elif sales > 10000:
    if town == "Sofia":
        comossion_percentage = 12
    elif town == "Varna":
        comossion_percentage = 13
    elif town == "Plovdiv":
        comossion_percentage = 14.5

if comossion_percentage == 0:
    print("error")
else:
    commission = sales * comossion_percentage / 100
    print(f"{commission:.2f}")