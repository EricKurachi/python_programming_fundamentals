"""
The sum of the first n positive integers can be computed by the
formula
sum(1..n) = 1 + 2 + 3 + 4 + · · · + n = n(n + 1)/2
Write a short Python program that computes the sum of the first 100 positive
integers and prints it to the screen in the format shown below. Use variables
to represent the 1, the 100, and the result of the computation. Your program
must compute the 5050 value. You cannot just print the result to the screen.
You must compute it first from the 100.
sum (1..100)=5050
"""

first_number = 1
last_number = 100
summ = last_number * (last_number + 1)/2

print('sum (' + str(first_number) + '..' + str(last_number) + ')', '=', summ)
