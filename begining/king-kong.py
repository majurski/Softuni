budget = float(input())
statisti = int(input())
pricecloth = float(input())

pricedekor = budget*0.10

if statisti > 150:
	pricecloth -= pricecloth*0.10

allcustomes = statisti*pricecloth

totalcost = allcustomes + pricedekor

money = abs(budget - totalcost)

if budget < totalcost:
	print("Not enough money!")
	print(f"Wingard needs {money:.2f} leva more.")
else:
	print("Action!")
	print(f"Wingard starts filming with {money:.2f} leva left.")