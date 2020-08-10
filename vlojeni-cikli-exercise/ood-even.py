n1 = int(input())
n2 = int(input())

for number in range(n1, n2 + 1):
    number_as_string = str(number)
    even_sum = 0
    odd_sum = 0

    for i in range(0, len(number_as_string)):
        digit = int(number_as_string[i])
        if (i + 1) % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if even_sum == odd_sum:
        print(number, end=" ")

