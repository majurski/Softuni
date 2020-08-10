population = int(input())
years = int(input())

for i in range(1, years+1):
    population += (population // 100) * 2
    if i % 2 == 0:
        population -= (population // 1000) * 10
    population -= (population // 200) * 2

print(f"People population: {population}")