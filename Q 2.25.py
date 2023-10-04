Employee = input("Enter employee's name: ")
hours = int(input('Enter hours worked in a week: '))
pay = float(input('Enter hourly pay rate: '))
fed_tax = float(input('Enter federal withholding rate: '))
state_tax = float(input('Enter state tax withholding rate: '))
 
print(f"Employee's name: {Employee}")
print(f'Pay Rate: ${pay}')
gross_pay = pay * hours
print(f'Gross Pay: ${gross_pay}')
tax1 = gross_pay * fed_tax
tax2 = gross_pay * state_tax
total_deduct = tax1 + tax2
print(f'Deductions:\n\tFederal Withholding: ${tax1:.2f} \n\tState Withholding: ${tax2:.2f} \n\tTotal Deductions: ${total_deduct:.2f}')
print(f'\nNet pay: ${gross_pay - total_deduct:.2f}')