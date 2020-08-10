from itertools import permutations

path = input()
possibilities = ["L","R","S"]

missing = 0
indeces = []

for i in path:
    if i == "*":
        missing += 1

for i in range(len(path)):
    if path[i] == "*":
        indeces.append(i)

# print(missing)
# print(indeces)
nposibble = 3**missing
print(nposibble)

comb = permutations(possibilities)
for i in comb:
    print(list(i))