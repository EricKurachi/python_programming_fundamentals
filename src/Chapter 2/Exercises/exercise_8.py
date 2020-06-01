"""
Write a program that prompts the user to enter an integer and then prints its hexadecimal equivalent.
Traditionally, hexadecimal numbers start with a “0x” to identify them as hex, so your output should look like this:
Please enter an integer: 255
The hexadecimal equivalent is 0x00ff
Your program should handle any base 10 integer from 0 to 65535. There is a
You should check the input that the user enters to make sure that it is in the valid
range accepted by your program.
"""

try:
    decimal = int(input("Please enter an integer: "))
except ValueError:
    print("Invalid value")
    exit(0)

if not 0 < decimal < 65535:
    print("The number should be positive and less than 65536")
    exit(0)

hexadecimal = ''

if (decimal % 16) >= 10:
    hexadecimal = chr(87 + decimal % 16) + hexadecimal
else:
    hexadecimal = str(decimal % 16) + hexadecimal

decimal = decimal // 16

if (decimal % 16) >= 10:
    hexadecimal = chr(87 + decimal % 16) + hexadecimal
else:
    hexadecimal = str(decimal % 16) + hexadecimal

decimal = decimal // 16

if (decimal % 16) >= 10:
    hexadecimal = chr(87 + decimal % 16) + hexadecimal
else:
    hexadecimal = str(decimal % 16) + hexadecimal

decimal = decimal // 16

if (decimal % 16) >= 10:
    hexadecimal = chr(87 + decimal % 16) + hexadecimal
else:
    hexadecimal = str(decimal % 16) + hexadecimal

decimal = decimal // 16

print('0x' + hexadecimal)
