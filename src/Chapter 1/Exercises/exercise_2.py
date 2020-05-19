"""
Write a program that capitalizes the first four characters of a string by converting
the characters to their ASCII equivalent, then adding the necessary amount to capitalize them,
and converting the integers back to characters. Print the capitalized
string. Here is a sample of running this program.
Please enter a four character string : kent
The string capitalized is KENT
"""

word = input("Please enter a four character string: ")

capitalized = (chr(ord(word[0]) - 32) +
               chr(ord(word[1]) - 32) +
               chr(ord(word[2]) - 32) +
               chr(ord(word[3]) - 32) +
               word[4:])

print("The string capitalized is {}".format(capitalized))
