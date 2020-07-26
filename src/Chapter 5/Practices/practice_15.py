"""
Write a recursive function that computes the nth Fibonacci number.
"""

def fibonacci(n):
    # base case
    if n == 1:
        return 1
    elif n == 0:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

# fibonacci(10) -> 89