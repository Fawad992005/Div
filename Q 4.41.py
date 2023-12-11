
while True:
   numbers = []
   for i in range(5):
        number = int(input(f"Enter {i + 1} number (enter 0 to stop): "))
        if number == 0:
            break
        numbers.append(number)
   if numbers:
        largest_number = max(numbers)
        counting = numbers.count(largest_number)
        print("Largest number:", largest_number)
        print("Count:", counting)
   else:
        print("No numbers entered. Exiting.")
        break
        




