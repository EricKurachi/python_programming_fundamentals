"""
Write a function called evenlyDividesList that returns true if
every element of a list given to the function is evenly divided by an integer
given to the function.
"""

def evenlyDividesList(lst, divisor):
    for i in lst:
        if i % divisor != 0:
            return False
    return True

print(evenlyDividesList([2,4,8], 2))  # True
print(evenlyDividesList([2,6,9], 3))  # False