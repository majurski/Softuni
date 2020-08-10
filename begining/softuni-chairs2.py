size = 7

width = int(size)

height = int(size + size / 2)

for i in range(width):
	for j in range(height):
		if (i + j) % 4 == 0:
			print("#")
		else:
			print(".")