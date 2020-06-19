"""
Write a program that asks the user to enter a list of integers one at a time. It should
allow the user to terminate the list by entering a − 1. Running the program would
look something like this.
"""

print("Enter a list of integers terminated by a -1")

try:
    number = int(input("Please enter the first integer and press enter: "))
except ValueError:
    print("Sorry the value entered is invalid")
    exit(0)

number_list = []

while number != -1:
    number_list.append(number)
    try:
        number = int(input("Please enter another integer: "))
    except ValueError:
        print("Sorry the value entered is invalid")
        exit(0)

print("The list of integers is", number_list)
