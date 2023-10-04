invest = int(input('Enter investment amount: '))
interest = float(input(f'Enter annual interest rate: '))
number_of_years = int(input('Enter number of years: '))
futureinvestmentvalue = invest * (1 + interest)**number_of_years*12
Accumulated_value = futureinvestmentvalue
print(f'The accumulated value is {Accumulated_value}. ')