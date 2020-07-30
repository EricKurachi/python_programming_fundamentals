"""
Write a function called sumIt which is given a list of numbers and returns the
sum of those numbers.
"""

def sum_it(num_list):
    sum = 0
    for n in num_list:
        sum += n
    return sum

if __name__ == "__main__":
    print(sum_it([1, 2, 5]))