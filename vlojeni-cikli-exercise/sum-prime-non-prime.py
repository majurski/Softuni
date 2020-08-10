line = input()
sum_primes = 0
sum_non_primes = 0

while line != "stop":

    if int(line) < 0:
        print("Number is negative.")
    elif int(line) > 1:
        for b in range(2, int(line)):
            if (int(line) % b) == 0:
                sum_non_primes += int(line)
                break
        else:
            sum_primes += int(line)



    line = input()


print(f"Sum of all prime numbers is: {sum_primes}")
print(f"Sum of all non prime numbers is: {sum_non_primes}")
