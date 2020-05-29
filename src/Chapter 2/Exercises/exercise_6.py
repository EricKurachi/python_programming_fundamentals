"""
Write a program that converts a decimal number to its binary equivalent. The
decimal number should be read from the user and converted to an int. Then you
should follow the algorithm presented in Example 1.1 to convert the decimal
number to its binary equivalent. The binary equivalent must be a string to get the
correct output. In this version of the program you must handle all 16-bit signed
integers. That means that you must handle numbers from −32768 to 32767. In
this version of the program you should not print any leading 0’s. Leading 0’s
should be omitted from the output.
If you want to check your work, you can use the bin function. The bin function will
take a decimal number and return a string representation of that binary number.
However, you should not use the bin function in your solution.
The output from the program must be identical to this:
Please enter a number : 83
The binary equivalent of 83 is 1010011.
"""

try:
    decimal_input = int(input("please enter a decimal number between -32768 and 32767: "))
except ValueError:
    print("Invalid number")
    exit(0)

if not -32768 < decimal_input < 32767:
    print("number out of range")
    exit(0)

decimal_number = abs(decimal_input)

to_binary = str(decimal_number % 2)
decimal_number = int(decimal_number / 2)

to_binary = str(decimal_number % 2) + to_binary
decimal_number = int(decimal_number / 2)

to_binary = str(decimal_number % 2) + to_binary
decimal_number = int(decimal_number / 2)

to_binary = str(decimal_number % 2) + to_binary
decimal_number = int(decimal_number / 2)

to_binary = str(decimal_number % 2) + to_binary
decimal_number = int(decimal_number / 2)

to_binary = str(decimal_number % 2) + to_binary
decimal_number = int(decimal_number / 2)

to_binary = str(decimal_number % 2) + to_binary
decimal_number = int(decimal_number / 2)

to_binary = str(decimal_number % 2) + to_binary
decimal_number = int(decimal_number / 2)

to_binary = str(decimal_number % 2) + to_binary
decimal_number = int(decimal_number / 2)

to_binary = str(decimal_number % 2) + to_binary
decimal_number = int(decimal_number / 2)

to_binary = str(decimal_number % 2) + to_binary
decimal_number = int(decimal_number / 2)

to_binary = str(decimal_number % 2) + to_binary
decimal_number = int(decimal_number / 2)

to_binary = str(decimal_number % 2) + to_binary
decimal_number = int(decimal_number / 2)

to_binary = str(decimal_number % 2) + to_binary
decimal_number = int(decimal_number / 2)

to_binary = str(decimal_number % 2) + to_binary
decimal_number = int(decimal_number / 2)

to_binary = str(decimal_number % 2) + to_binary
decimal_number = int(decimal_number / 2)

if decimal_input < 0:
    to_binary = 1111111111111111 - int(to_binary)
    to_binary = str(to_binary)
    if to_binary[-1] == '0':
        to_binary = int(to_binary) + 1
    elif to_binary[-2] == '0':
        to_binary = int(to_binary) + 9
    elif to_binary[-3] == '0':
        to_binary = int(to_binary) + 89
    elif to_binary[-4] == '0':
        to_binary = int(to_binary) + 889
    elif to_binary[-5] == '0':
        to_binary = int(to_binary) + 8889
    elif to_binary[-6] == '0':
        to_binary = int(to_binary) + 88889
    elif to_binary[-7] == '0':
        to_binary = int(to_binary) + 888889
    elif to_binary[-8] == '0':
        to_binary = int(to_binary) + 8888889
    elif to_binary[-9] == '0':
        to_binary = int(to_binary) + 88888889
    elif to_binary[-10] == '0':
        to_binary = int(to_binary) + 888888889
    elif to_binary[-11] == '0':
        to_binary = int(to_binary) + 8888888889
    elif to_binary[-12] == '0':
        to_binary = int(to_binary) + 88888888889
    elif to_binary[-13] == '0':
        to_binary = int(to_binary) + 888888888889
    elif to_binary[-14] == '0':
        to_binary = int(to_binary) + 8888888888889
    elif to_binary[-15] == '0':
        to_binary = int(to_binary) + 88888888888889
    elif to_binary[-16] == '0':
        to_binary = int(to_binary) + 888888888888889
    else:
        to_binary = int(to_binary) + 8888888888888889

print(int(to_binary))
