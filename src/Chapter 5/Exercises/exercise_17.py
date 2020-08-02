"""
Write a function called sumRange that given two integers returns the sum of
all the integers between the two given integers inclusive.
"""

def sum_it(num_list):
    sum = 0
    for n in num_list:
        sum += n
    return sum


def sum_range(first, last):
    num_list = []
    for i in range(first, last + 1):
        num_list.append(i)
    return sum_it(num_list)


if __name__ == "__main__":
    print(sum_range(3,6))
