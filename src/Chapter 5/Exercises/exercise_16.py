"""
Write a function called isPerfect that given an integer returns True if the number
is the sum of its factors (not including itself) and False otherwise.
"""

def factors(n):
    i = 1
    factors_list = []
    while i <= n/2:
        if n % i == 0:
            factors_list.append(i)
        i += 1
    # factors_list.append(n)
    return factors_list


def sum_factors(n):
    sum = 0
    for n in factors(n):
        sum += n
    return sum


def is_perfect(n):
    if sum_factors(n) == n:
        return True
    return False


if __name__ == "__main__":
    print(is_perfect(6))