number = int(input(""))
thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
ones = number % 10
palace = (thousands == ones) and (hundreds == tens)
print(palace)