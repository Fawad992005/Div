def smallest_factors(number):
    smallest_factors_list = []
    for i in range(2, number + 1):
        while number % i == 0:
            smallest_factors_list.append(i)
            number //= i
    return smallest_factors_list

n = int(input("Enter a number: "))
result = smallest_factors(n)
print(f"The factors of {n} are: {result}")
