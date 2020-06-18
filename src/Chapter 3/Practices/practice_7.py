"""
A program that prints out the characters of a string in reverse order.
"""

s = input("Please enter a string: ")

for i in range(len(s) - 1, -1, -1):
    print(s[i])
