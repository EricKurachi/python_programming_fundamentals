"""
Write a program that prompts the user to enter a 16-bit binary number (a string
of 1’s and 0’s). Then, the program should print the decimal equivalent. Be sure
to handle both negative and positive binary numbers correctly. If the user enters
less than 16 digits you should assume that the digits to the left of the last digit
are zeroes. When run the output should look like this:
Please enter a 16 - bit binary number : 1010011
The base 10 equivalent of the binary number 1010011 is 83.
To handle negative numbers correctly you first need to detect if it is a negative
number. A 16-digit binary number is negative if it is 16 digits long and the leftmost digit is a 1.
To convert a negative number to its integer equivalent, first take
the 1’s complement of the number. Then convert the 1’s complement to an integer,
then add 1 to the integer and negate the result to get the 2’s complement.
The conversion from bits to an integer can be carried out by multiplying each bit
by the power of 2 that it represents as described in Sect.1.5 of Chap. 1
"""
flag = ''

binary_number = input("Please enter a 16-bit binary number: ")
if len(binary_number) != 16:
    print("Wrong size")
    exit(0)

if binary_number[0] == '1':
    binary_number = (1111111111111111 - int(binary_number))
    flag = 'negative'

binary_number = str(binary_number).zfill(16)

decimal = int(binary_number[0]) * (2 ** 15)
decimal += int(binary_number[1]) * (2 ** 14)
decimal += int(binary_number[2]) * (2 ** 13)
decimal += int(binary_number[3]) * (2 ** 12)
decimal += int(binary_number[4]) * (2 ** 11)
decimal += int(binary_number[5]) * (2 ** 10)
decimal += int(binary_number[6]) * (2 ** 9)
decimal += int(binary_number[7]) * (2 ** 8)
decimal += int(binary_number[8]) * (2 ** 7)
decimal += int(binary_number[9]) * (2 ** 6)
decimal += int(binary_number[10]) * (2 ** 5)
decimal += int(binary_number[11]) * (2 ** 4)
decimal += int(binary_number[12]) * (2 ** 3)
decimal += int(binary_number[13]) * (2 ** 2)
decimal += int(binary_number[14]) * (2 ** 1)
decimal += int(binary_number[15]) * (2 ** 0)

if flag == 'negative':
    decimal = '-' + str(decimal + 1)
    print("Negative decimal")

print(decimal)

