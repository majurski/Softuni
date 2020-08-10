screenig_type = input()
rows = int(input())
cols = int(input())

income = 0

cinema_capacity = rows * cols

if screenig_type == "Premiere":
    income = cinema_capacity * 12.00
elif screenig_type == "Normal":
    income = cinema_capacity * 7.50
elif screenig_type == "Discount":
    income = cinema_capacity * 5.00

print(f"{income:.2f} leva")