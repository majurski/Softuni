new = input()

bunk = []
for i in new:
	counter = new.count(i)
	ser = i
	cash = str(f'{ser} - {counter} times')
	bunk.append(cash)
	
bunk = set(bunk)
for c in bunk:
	print(c)