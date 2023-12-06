import math
def get_distance(x1,y1,x2,y2):
    difx = (x2 - x1)
    dify = (y2 - y1)
    p = math.pow(difx,2) + math.pow(dify,2)
    s = math.sqrt(p)
    return s



x1 = 0
y1 = 0
x2 = int(input("Enter value of x2: "))
y2 = int(input("Enter value of y2: "))

if get_distance(x1,y1,x2,y2)<=10:
    print(f"Point {x2},{y2} is in circle")
else:
    print(f"Point {x2},{y2} is outside the circle")
