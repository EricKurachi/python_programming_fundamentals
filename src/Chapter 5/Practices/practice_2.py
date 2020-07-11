"""
Write a function called implode that given a list of characters,
or strings, returns a string which is the concatenation of those characters, or
strings.
"""

def implode(char_list):
    concatenation = ''
    for char in char_list:
        concatenation += char
    return concatenation

print(implode(['S', 'u', 'd', 'o', 'k', 'u']))