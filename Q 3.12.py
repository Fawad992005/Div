while True:
    num = int(input('Enter a number: '))
    if num%5==0 and num%6==0:
        print(f'{num} is divisible by both 5 & 6.')
    elif num%5==0:
        print(f'{num} is divisible by 5 only.')
    elif num%6==0:
        print(f'{num} is divisible by 6 only.')
    else:
        print(f'{num} is not divisible by both 5 & 6.')
    cont = input('Do you want to continue(Y/N): ')
    if cont.upper() != 'Y' and cont.upper() != 'YES':
        break
        
    