"""
Write a program that asks the user to enter a list of numbers and then prints the
count of the numbers in the list and the average of the numbers in the list. Do
not use the len function to find the length of the list. Use the accumulator pattern
instead.
"""

numbers = input("Please enter a list of numbers: ")

acc = 0
length = 0

for i in numbers.split():
    length += 1
    acc += float(i)

print("The average is", acc/length)
