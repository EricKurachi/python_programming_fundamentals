"""
What would happen if the base case and the recursive case
were written in the opposite order in Example 5.13?
"""

"""
def factorial(n):
    return n * factorial(n - 1)

    if n == 0:
        return 1

print(factorial(5))
""" 
    
# It would return an error, because the recursive case is always called and enters again in the function never checking the base case.
