import math

def wind_temp(temp,speed):
    ta = temp
    v = speed
    to = 35.74 + (0.6215*ta) - (35.75*math.pow(v,0.16)) + (0.4275*ta*math.pow(v,0.16))
    return to

while True:
    try:
      temp = float(input("Enter temperature in Farenheit between -58F and 48F: "))
      speed = float(input("Enter Wind speed in miles per hour greater than  or equal to 2: "))
      if -58 <= temp <= 48 and speed >= 2:
         break
      else:
         print("Error!!!.Enter temperature and speed within given range.")
    except ValueError:
       print("Wrong input try again!")

result = wind_temp(temp,speed)
print(f"The wind chill index is {result:.2f}")

