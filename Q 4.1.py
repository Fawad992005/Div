def average(number):
    if len(number) == 0:
        return 0  # Avoid division by zero if the list is empty
    return sum(number) / len(number)


def positives(num):
    p = []
    for i in num:
      if i > 0:
          p.append(i)
    return p



def negatives(num):
    n = []
    for i in num:
      if i < 0:
          n.append(i)
    return n

l = []

for i in range(5):
    num =  int(input(f"Enter {i+1} number: "))
    l.append(num)
    
    if num == 0:
        break   

total = len(l)
print(f"The total is {total}")
negative = negatives(l) 
positive = positives(l)
print(f"The negatives are {negative}")
print(f"The possitives are {positive}")
avg = average(l)
print(f"The average is {avg}")

