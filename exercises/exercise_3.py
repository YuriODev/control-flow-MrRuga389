num = int(input("what is your number: "))
remainder = num//2
if num < 0 or num > 36:
    print("The bet will not play!")
elif num == 0: 
    print("Green")
elif num < 10:
    if remainder == 0:
        print("Black")
    else:
        print("Red")
elif num < 18:
    if remainder == 0:
        print("Red")
    else:
        print("Black")
elif num < 28:
    if remainder == 0:
         print("Black")
    else:
        print("Red")
elif num < 36:
    if remainder == 0:
        print("Red")
    else:
        print("Black")


