"""
Write a program that converts a decimal number to its binary equivalent. The
decimal number should be read from the user and converted to an int. Then you
should follow the algorithm presented in Example 1.1 to convert the decimal
number to its binary equivalent. The binary equivalent must be a string to get the
correct output. The output from the program must be identical to this:

Please enter a number: 83
The binary equivalent of 83 is 01010011.

You may assume that the number that is entered is in the range 0–255. If you
want to check your work, you can use the bin function. The bin function will
take a decimal number and return a string representation of that binary number.
However, you should not use the bin function in your solution (Fig. 1.23).
"""

decimal_number = int(input("Please enter a number: "))
binary_equivalent = ''

# The loop version of this program is in the practice_2. Just made with what the book provided here
binary_equivalent += str(decimal_number % 2)
decimal_number = int(decimal_number/2)

binary_equivalent = str(decimal_number % 2) + binary_equivalent
decimal_number = int(decimal_number/2)

binary_equivalent = str(decimal_number % 2) + binary_equivalent
decimal_number = int(decimal_number/2)

binary_equivalent = str(decimal_number % 2) + binary_equivalent
decimal_number = int(decimal_number/2)

binary_equivalent = str(decimal_number % 2) + binary_equivalent
decimal_number = int(decimal_number/2)

binary_equivalent = str(decimal_number % 2) + binary_equivalent
decimal_number = int(decimal_number/2)

binary_equivalent = str(decimal_number % 2) + binary_equivalent
decimal_number = int(decimal_number/2)

binary_equivalent = str(decimal_number % 2) + binary_equivalent
decimal_number = int(decimal_number/2)

print("The binary equivalent of {} is {}.".format(decimal_number, binary_equivalent))
