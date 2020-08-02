"""
Write a function called sumFactors that given an integer returns the sum of
the factors of that integer
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


def sum_factors(n):
    sum = 0
    for n in factors(n):
        sum += n
    return sum


if __name__ == "__main__":
    print(sum_factors(6))