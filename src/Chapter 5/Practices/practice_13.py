"""
Recalling that each time a function is called an activation record
is pushed on the run-time stack, how many activation records will be pushed
on the run-time stack at its deepest point when computing factorial (5)?
"""

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

# Seven times