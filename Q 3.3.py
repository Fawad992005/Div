#Function to find x
def forx(li):
     denominator = li[0] * li[3] - li[1] * li[2]
     if denominator == 0:
         return f"equation has no solution "
     else:
         x = (li[4]*li[3]-li[1]*li[5])/denominator
         return x
def fory(li):
     denominator = li[0] * li[3] - li[1] * li[2]
     if denominator == 0:
          return f"equation has no solution "
     else:
          y = (li[0]*li[5]-li[4]*li[2])/denominator
          return y
for i in range(6):
    try:
      li = []
      a = li.append(float(input("Enter value of a: ")))
      b = li.append(float(input("Enter value of b: ")))
      c = li.append(float(input("Enter value of c: ")))
      d = li.append(float(input("Enter value of d: ")))
      e = li.append(float(input("Enter value of e: ")))
      f = li.append(float(input("Enter value of f: ")))
      break
    except ValueError:
        print("Enter an integer value!!!! ")
        continue

print(f"Y is {fory(li)} and X is {forx(li)}")
