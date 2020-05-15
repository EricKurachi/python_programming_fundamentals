""" Decimal to binary """

remainders = ''
decimal_number = 58
quotient = decimal_number

while quotient != 0:
    remainders += str(quotient % 2)
    quotient = int(quotient/2)

binary = remainders[::-1]
print(binary)




