"""
Find the negative of a binary number. Only works with numbers ended in 1
"""

binary_number = 0b01010011
binary_number_str = '01010011'

# Using 2's complement

complement = ''

for digit in binary_number_str:
    complement += str((int(digit) + 1) % 2)
complement = int(complement) + 1

print(complement)
