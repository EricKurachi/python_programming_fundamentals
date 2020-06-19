"""
Write a program that asks the user to enter a list of numbers. The program should
take the list of numbers and add only those numbers between 0 and 100 to a new
list. It should then print the contents of the new list. Running the program should
look something like this:
"""

numbers = input("Please enter a list of numbers: ")

acc = 0
hundred = []

for i in numbers.split():
    if 0 < int(i) < 100:
        hundred.append(i)

print("The new list is", hundred)
