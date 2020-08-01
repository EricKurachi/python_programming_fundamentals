"""
Use bottom-up design to write a program with three functions that capitalizes
the first letter of each word in a sentence
"""

# First function defined
def capitalize_first_letter(word):
    return word[0].upper() + word[1:]


# Second function defined
def capitalize_initials(phrase):
    words = ''
    words_list = phrase.split()
    for word in words_list:
        words += capitalize_first_letter(word) + ' '
    return words


# Third function defined
def main():
    phrase = input("Please insert a phrase: ")
    print(capitalize_initials(phrase))


if __name__ == "__main__":
    main()
