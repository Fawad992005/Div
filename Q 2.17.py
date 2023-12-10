import math

def wind_temp(temp,speed):
    ta = temp
    v = speed
    to = 35.74 + (0.6215*ta) - (35.75*math.pow(v,0.16)) + (0.4275*ta*math.pow(v,0.16))
    return to

while True:
    try:
        temp = float(input("Enter temperature in Fahrenheit between -58°F and 48°F: "))
        if -58 <= temp <= 48:
            break
        else:
            print("Error!!! Enter temperature within the given range.")
            continue

    except ValueError:
        print("Wrong input! Try again.")

while True:
    try:
        speed = float(input("Enter wind speed in miles per hour, greater than or equal to 2: "))
        if speed >= 2:
            break
        else:
            print("Error!!! Enter speed within the given range.")
    except ValueError:
        print("Wrong input! Try again.")

result = wind_temp(temp,speed)
print(f"The wind chill index is {result:.2f}")

