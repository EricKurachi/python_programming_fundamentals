"""
Write a program that converts a binary number to its decimal equivalent. The
binary number will be entered as a string. Use the powers of 2 to convert each of
the digits in the binary number to its appropriate power of 2 and then add up the
powers of two to get the decimal equivalent. When the program is run, it should
have output identical to this:
Please enter an eight digit binary number: 01010011
The decimal equivalent of 01010011 is 83.
"""

binary_number = input("Please enter an eight digit binary number: ")
decimal_equivalent = 0

# The loop version of this program is in the practice 1. Just wanted to use what was given at this point in the book
decimal_equivalent += int(binary_number[7]) * (2 ** 0)
decimal_equivalent += int(binary_number[6]) * (2 ** 1)
decimal_equivalent += int(binary_number[5]) * (2 ** 2)
decimal_equivalent += int(binary_number[4]) * (2 ** 3)
decimal_equivalent += int(binary_number[3]) * (2 ** 4)
decimal_equivalent += int(binary_number[2]) * (2 ** 5)
decimal_equivalent += int(binary_number[1]) * (2 ** 6)
decimal_equivalent += int(binary_number[0]) * (2 ** 7)

print("The decimal equivalent of {} is {}.".format(binary_number, decimal_equivalent))
