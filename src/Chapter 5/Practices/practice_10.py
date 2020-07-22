"""
Using the last version of the evenlyDivides function, write a
function called evenlyDivisibleElements that given an integer, x, and a list of
integers, returns the list of integers from the given list that evenly divide x.
"""

def evenlyDivides(x, y):
    return y % x == 0

def evenlyDivisibleElements(x, lst):
    divisors = []
    for element in lst:
        if evenlyDivides(element, x):
            divisors.append(element)
    return divisors

print(evenlyDivisibleElements(10, [1,2,3,4,5]))  # [1, 2, 5]  