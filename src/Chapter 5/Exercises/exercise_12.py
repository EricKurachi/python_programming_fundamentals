"""
Use top-down design to write a program with three functions that capitalizes
the first letter of each word in a sentence.
"""

# Third function defined
def capitalize_first_letter(word):
    return word[0].upper() + word[1:]


# Second function defined
def capitalize_initials(phrase):
    capitalized = ''
    words_list = phrase.split()
    for word in words_list:
        capitalized += capitalize_first_letter(word) + ' '
    return capitalized


# First function defined
def main():
    phrase = input("Please enter a phrase: ")
    print(capitalize_initials(phrase))


if __name__ == "__main__":
    main()
