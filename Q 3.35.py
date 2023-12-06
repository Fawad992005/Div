def hexa_decimal(n):
    dec_hexa = hex(n)
    dec_hexarep= dec_hexa.upper()
    return dec_hexarep[2:]


while True:
    try:
        n = int(input("Enter an integer between (0-15): "))
        if 0 <= n <= 15:
            break
        else:
            print("Please enter a valid integer between 0 and 15.")
    except ValueError:
        print("Please enter a valid integer between 0 and 15.")
        print("Wrong input try again!!")
        continue


result = hexa_decimal(n)
print(result)

