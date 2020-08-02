"""
Write a function called oddElements that given a list, returns a list containing
only the odd elements of the list. The first element of a list (i.e. index 0) is an
even element.
"""

def odd_elements(l):
    new_l = []
    for i in range(1, len(l), 2):
        new_l.append(l[i])
    return new_l

if __name__ == "__main__":
    print(odd_elements([1, 2, 3, 4]))