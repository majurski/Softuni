number_bees = int(input())
number_flow = int(input())

all_honey = number_bees * number_flow * 0.21

honeycombs = all_honey // 100

left = all_honey - honeycombs*100

print(f"{honeycombs:.0f} honeycombs filled.")
print(f"{left:.2f} grams of honey left.")
