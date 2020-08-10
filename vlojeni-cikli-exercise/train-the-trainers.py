n = int(input())
type_assess = input()
mid = 0
mid_end = 0
counter = 0

while type_assess != "Finish":
    sum_asss = 0
    counter += 1
    for i in range(1, n + 1):
        asesment = float(input())
        sum_asss += asesment
        avr_ass = sum_asss / n

    print(f"{type_assess} - {avr_ass:.2f}.")
    mid += avr_ass
    mid_end = mid / counter
    type_assess = input()

print(f"Student's final assessment is {mid_end:.2f}.")



