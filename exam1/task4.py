import math

population = int(input())
years = int(input())


for i in range(1, years + 1):

    izlupeni = (population // 10) * 2
    population += izlupeni

    if i % 5 == 0 and i != 0:
        migrate = (population // 50) * 5
        population -= migrate
        population -= death

    if i == years:
        break

    death = (population // 20) * 2
    population -= death


print(f"Beehive population: {population}")