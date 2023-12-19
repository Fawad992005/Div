def is_perfect_number(number):
    factor_sum = 0
    for i in range(1, number):
        if number % i == 0:
           factor_sum += i
    return factor_sum == number

for i in range(1, 10000):
    if is_perfect_number(i):
        print(f"{i} is a perfect number.")
