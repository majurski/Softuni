age = int(input())
price_washing = float(input())
price_of_toy = int(input())

money = 0
money_brother = 0
b = 0
c = 1
for i in range(0, age - 1):
    if i % 2 == 0:
        money_brother += 1
        b += 1
        money += b*10
    else:
        c += 1
        money_from_toy = c*price_of_toy


all_money = money + money_from_toy - money_brother

dif = abs(all_money-price_washing)
if all_money >= price_washing:
    print(f"Yes! {dif:.2f}")
else:
    print(f"No! {dif:.2f}")