"""
Write a function called oddCharacters that given a string, returns a string containing only the odd characters of the given string.
"""

def odd_characters(s):
    new_s = ''
    for i in range(1, len(s), 2):
        new_s += s[i]
    return new_s

if __name__ == "__main__":
    print(odd_characters('hi there'))

