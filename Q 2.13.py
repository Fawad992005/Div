#Financial Application
savings = int(input('Enter saving amount: '))
annual_interest = '5%'
monthly_interest = 0.05/12
M1 = savings * (1 + 0.00417)
M2 = (savings + M1) * (1 + 0.00417)
M3 = (savings + M2) * (1 + 0.00417)
M4 = (savings + M3) * (1 + 0.00417)
M5 = (savings + M4) * (1 + 0.00417)
M6 = (savings + M5) * (1 + 0.00417)
print(f'After sixth month the account value is ${M6}.')