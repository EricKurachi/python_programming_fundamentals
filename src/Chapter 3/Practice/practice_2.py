"""
Write a program that asks the user to
enter “yes” or “no”. If they enter a string with any capital letters the program
should print a message that says, “Next time please use all lower case letters”.
"""

s = input("Please enter 'yes' or 'no': ")

if not s.islower():
    print("Next time please use all lower case letters")
