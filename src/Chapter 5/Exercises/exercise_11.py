"""
Write a recursive function called recursiveSumIt which given a list of numbers,
returns the sum of those numbers.
"""

def recursive_sum_it(num_list):
    if type(num_list) == int:
        return num_list
    elif len(num_list) == 1:
        return num_list[0]
    else:
        return recursive_sum_it(num_list[0]) + recursive_sum_it(num_list[1:])

if __name__ == "__main__":
    print(recursive_sum_it([3, 2, 4, 8]))