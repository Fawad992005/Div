def calc(number):
    if number % 5 == 0 and number % 6 == 0:
        return number

result_list = []

for i in range(100, 1001):
    calculated_value = calc(i)
    if calculated_value is not None:
        result_list.append(calculated_value)

for i in range(0, len(result_list), 10):
    print(result_list[i:i+10])

    