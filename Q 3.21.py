def get_century(k):
    return  k//100

def get_dayofweek(k,m,q):
    d = ['Friday','Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday']
    h = (q + (26*(m+1)//10)+ k + (k//4) + (get_century(k)//4) + (5*get_century(k))) % 7
    return d[h]



for i in range(3):
    try:
      k = int(input("Enter year: "))
      m = int(input("Enter month: "))
      q = int(input("Enter day of the month: "))
      break
    except ValueError:
        print("Wrong input ,Try again!!")
        continue


print(get_dayofweek(k,m,q))