x1, y1 = int(input("")), int(input(""))
x2, y2 = int(input("")), int(input(""))
x3, y3 = int(input("")), int(input(""))
a2 = (x2-x1)**2 + (y2-y1)**2
b2 = (x3-x2)**2 + (y3-y2)**2
c2 = (x1-x3)**2 + (y1-y3)**2
if a2 == 0 or b2 == 0 or c2 == 0:
    print("No")
elif a2 + b2 == c2 or b2 + c2 == a2 or c2 + a2 == b2:
    print("Yes")
else:
    print("No")
