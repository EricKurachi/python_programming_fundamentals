"""
Write a function called dotProduct that computes the dot product of two lists of
numbers given to the function.
"""

def zip(list_1, list_2):
    tuples_list = []
    j = 0
    for i in list_1:
        tuples_list.append((i, list_2[j]))
        j += 1
    return tuples_list


def dot_product(a, b):
    result = 0
    zipped = zip(a, b)
    for pair in zipped:
        result += pair[0] * pair[1]
    return result

if __name__ == "__main__":
    print(dot_product([8, 0], [3, 6]))