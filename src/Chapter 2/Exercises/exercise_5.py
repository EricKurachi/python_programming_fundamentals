"""
Write a program that asks the user to enter an integer less than 50 and then prints
whether or not that integer is prime. To determine if a number less than 50 is
prime you only need to divide by all prime numbers that are less than or equal to
the square root of 50. If any of them evenly divide the number then it is not prime.
Use the guess and check pattern to solve this problem. Use exception handling to
check the input from the user to be sure it is valid. A run of the program should
look like this:
Please enter an integer less than 50: 47
47 is prime.
"""

try:
    integer = int(input("Please enter an integer less than 50: "))
except ValueError:
    print("Invalid value")
    exit(0)

if not(0 < integer < 50):
    print("It must be positive and less than 50")
    exit(0)

guess = "is prime"

if integer == 1:
    guess = "isn't prime"

if integer != 2 and integer % 2 == 0:
    guess = "isn't prime"

if integer != 3 and integer % 3 == 0:
    guess = "isn't prime"

if integer != 5 and integer % 5 == 0:
    guess = "isn't prime"

if integer != 7 and integer % 7 == 0:
    guess = "is'n prime"

print("{} {}".format(integer, guess))
