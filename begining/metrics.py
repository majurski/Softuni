number = float(input())
vhod = input()
izhod = input()

if vhod == "mm":
	number /= 1000

elif vhod == "cm":
	number /= 100



if izhod == "mm":
	number *= 1000

elif izhod == "cm":
	number *= 100

print(f"{number:.3f}")

