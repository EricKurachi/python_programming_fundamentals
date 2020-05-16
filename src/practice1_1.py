"""
What is the decimal equivalent of the binary number 01010101?
"""

binary = '01010101'
decimal = 0
aux = 0

binary = binary[::-1]

for digit in binary:
    decimal += int(digit) * (2 ** aux)
    aux += 1

print(decimal)
