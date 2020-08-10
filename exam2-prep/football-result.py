result_1 = input()
result_2 = input()
result_3 = input()

win = 0
lose = 0
drawn = 0

if result_1[0] > result_1[2]:
    win += 1
if result_1[0] < result_1[2]:
    lose += 1
if result_1[0] == result_1[2]:
    drawn += 1

if result_2[0] > result_2[2]:
    win += 1
if result_2[0] < result_2[2]:
    lose += 1
if result_2[0] == result_2[2]:
    drawn += 1

if result_3[0] > result_3[2]:
    win += 1
if result_3[0] < result_3[2]:
    lose += 1
if result_3[0] == result_3[2]:
    drawn += 1


print(f"Team won {win} games.")
print(f"Team lost {lose} games.")
print(f"Drawn games: {drawn}")
