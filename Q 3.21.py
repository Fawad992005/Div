def get_dayofweek(year,month,day):
    d = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    h = (day + (13 * (month + 1) // 5) + year + (year // 4) - (year // 100) + (year // 400)) % 7
    return d[h]



for i in range(3):
    try:
      year = int(input("Enter year: "))
      month = int(input("Enter month: "))
      day = int(input("Enter day of the month(1-31): "))
      if 1 <= day <= 31:
        break
      else:
        print("Invalid day input, please try again.")
        continue
    except ValueError:
        print("Wrong input ,Try again!!")
        continue


print(get_dayofweek(year,month,day))
