"""
Write the algorithm so it will convert any 32-bit signed integer to its binary equivalent
"""

remainders = ''
decimal_number = int(input("Please enter a integer between −2^31 and 2^31 − 1: "))
quotient = decimal_number

if 0 <= decimal_number < 2 ** 31:
    while quotient != 0:
        remainders += str(quotient % 2)
        quotient = int(quotient/2)
    binary = remainders[::-1]

elif -2 ** 31 <= decimal_number < 0:
    while quotient != 0:
        remainders += str(quotient % 2)
        quotient = int(quotient/2)
    binary = remainders[::-1]
    reversed_bits = 11111111111111111111111111111111 - int(binary)
    binary = '0b' + str(reversed_bits)
    integer_sum = int(binary, 2) + int('0b1', 2)
    binary = bin(integer_sum)

else:
    print("This is not a valid input")
    exit(0)

print(binary)

