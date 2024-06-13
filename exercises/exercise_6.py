x2, y2 = int(input("Enter x2: ")), int(input("Enter y2: "))
da = x1**2 + y1**2

db = x2**2 + y2**2
if da > db:
    print("A is further from the origin.")
elif da < db:
    print("B is further from the origin.")
else:
    print("A and B are at the same distance from the origin.")