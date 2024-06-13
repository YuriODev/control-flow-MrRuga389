a = int(input(""))
b = a//100 + a%10
c = (a//10)%10
if b==c:
    print("=")
elif b>c:
    print(">")
else:
    print("<")

