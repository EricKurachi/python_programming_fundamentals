"""
Write a program that prints all the prime numbers less than 1,000. You can write
this program by creating a list of prime numbers. To begin, the list is empty. Then
you write two nested for loops. The outer for loop runs through all the numbers
from 2 to 999. The inner for loop runs through the list of prime numbers. If the
next number in the outer for loop is not divisible by any of the prime numbers,
then it is prime and can be printed as a prime and added to the list of primes. To
add an element, e, to a list, lst, you can write lst.append(e). This program uses
both the guess and check pattern and the accumulator pattern to build the list of
prime numbers.
"""

primes = []

for i in range(2, 1000):
    is_prime = True  # guess
    for j in primes:
        if j != 0 and i % j == 0:
            is_prime = False
    if is_prime:
        primes.append(i)

print(primes)
