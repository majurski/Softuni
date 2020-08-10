startZaplata = float(input())
razhodi = float(input())
narastva = float(input())

cena = float(input())
meseci = int(input())

bank = []
initial = startZaplata

for i in range(meseci -1):
	startZaplata += narastva
	bank.append(startZaplata)

erning = sum(bank) + initial
total = erning - meseci*razhodi

if total >= cena:
    print("Have a nice ride!")
else:
    print("Work harder!")