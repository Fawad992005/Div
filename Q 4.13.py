n = 0

while n**3 < 12000:
    n += 1

# Since we want the largest n, decrement by 1
n -= 1

print("The largest n such that cube of n is less than 12000 is:", n)
