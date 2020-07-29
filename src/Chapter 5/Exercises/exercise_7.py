"""
Write a function called isPrime that returns True if an integer given to the function
is a prime number.
"""

def is_prime(n):
    max_divisor = int(n**(1/2))
    for i in range(2, max_divisor):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Please enter a number: "))
    print(is_prime(n))

if __name__ == "__main__":
    main()