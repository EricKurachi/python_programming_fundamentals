"""
Write a function called factors that given an integer returns the list of the factors
of that integer.
"""

def factors(n):
    i = 1
    factors_list = []
    while i <= n/2:
        if n % i == 0:
            factors_list.append(i)
        i += 1
    factors_list.append(n)
    return factors_list

if __name__ == "__main__":
    print(factors(6))