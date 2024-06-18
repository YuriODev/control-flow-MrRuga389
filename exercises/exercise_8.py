a = int((input("")))
b = int(input(""))
c = False
if b == a//100:
    c = True
elif b == (a//10)%10:
    c = True
elif b == a%10:
    c = True
print(c)
    