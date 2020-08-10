amount_needed = float(input())
bee_name = input()
all_honey = 0

while bee_name != "Winter has come":
    for i in range(6):
        amount = float(input())
        all_honey += amount
    if all_honey < 0:
        print(f"{bee_name} was banished for gluttony")

    bee_name = input()

dif = abs(amount_needed - all_honey)

if amount_needed >= all_honey:
    print(f"Hard Winter! Honey needed {dif:.2f}.")
else:
    print(f"Well done! Honey surplus {dif:.2f}.")