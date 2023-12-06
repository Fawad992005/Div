import math

def get_horizontal(x1,y1,x2,y2):
    difx = (x2 - x1)
    dify = (y2 - y1)
    p = math.pow(difx,2) + math.pow(dify,2)
    s = math.sqrt(p)
    if s <= 10 and s <= 5:
        return True
    else:
        return False
    

def get_vertical(x1,y1,x2,y2):
    difx = (x2 - x1)
    dify = (y2 - y1)
    p = math.pow(difx,2) + math.pow(dify,2)
    s = math.sqrt(p)
    if s <= 5 and s <= 10:
        return True
    else:
        return True

x1 = 0
y1 = 0
x2 = float(input("Enter value of x2: "))
y2 = float(input("Enter value of y2: "))


v = get_vertical(x1,y1,x2,y2)
h = get_horizontal(x1,y1,x2,y2)
if v and h is True:
    print(f"Point {x2},{y2} is in rectangle.")
else:
    print(f"Point {x2},{y2} is not in rectangle")