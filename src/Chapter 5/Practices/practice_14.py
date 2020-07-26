"""
Run the factorial program on an input of 5 using Wing or
your favorite IDE. Set a breakpoint in the factorial function on the two return
statements. Watch the run-time stack grow and shrink. What do you notice
about the parameter n?
"""

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

# There are six different variables n going from 5 to 0 decrementing each function call