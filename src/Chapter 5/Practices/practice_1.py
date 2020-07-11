"""
Write a function called explode that given a string returns a list
of the characters of the string.
"""

def explode(s):
    characters = []
    for char in s:
        characters.append(char)
    return characters

print(explode('Sudoku'))