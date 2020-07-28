"""
Write a predicate function called isEven that returns True if a number is even
and False if it is not
"""

def is_even(n):
    if n % 2 == 0:
        return True
    return False

if __name__ == "__main__":
    print(is_even(4))