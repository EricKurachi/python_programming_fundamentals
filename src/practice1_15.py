"""
Re-do Practice Problem 1.14 using format specifiers when
printing instead of converting each item to a string. The goal is for the output
to look exactly the same.
sum (1..100)=5050
"""

first_number = 1
last_number = 100
summ = last_number * (last_number + 1)/2

print('sum ({0}..{1})={2:1d}'.format(first_number, last_number, summ))
