"""
The following code does not work. What is the error message?
Do you see why? Can you suggest a way to fix it?

def length(L):
    len = 1
    for i in range(len(L)):
        len = len + 1
    return len

print(length([1, 2, 3]))

# TypeError: 'int' object is not callable
# the len variable is overlapping the len built in method
"""

def length(L):
    l = 0
    for i in range(len(L)):
        l = l + 1
    return l

print(length([1, 2, 3]))