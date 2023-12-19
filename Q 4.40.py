import random as rd
l = ["Heads","Tails"]

Heads = 0
Tails = 0

for i in range(1000000):
    choice = rd.choice(l)
    if choice == "Heads":
        Heads += 1
    else:
        Tails += 1

print(f"The number of Heads is {Heads} and number of Tails is {Tails}")
