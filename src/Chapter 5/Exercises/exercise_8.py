"""
Write a function called zip that is given two lists of the same
length and creates a new list of two-tuples where each two-tuple is the tuple of
the corresponding elements from the two lists.
"""

def zip(list_1, list_2):
    tuples_list = []
    j = 0
    for i in list_1:
        tuples_list.append((i, list_2[j]))
        j += 1
    return tuples_list

if __name__ == "__main__":
    print(zip([1, 2, 3],[4, 5, 6]))