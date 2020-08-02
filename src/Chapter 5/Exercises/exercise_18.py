"""
Write a function called reverseWords that given a string representing a sentence,
returns the same sentence but with each word reversed.
"""

def reverse_words(phrase):
    new_phrase = ''
    for word in phrase.split():
        new_phrase += word[::-1] + ' '
    return new_phrase

if __name__ == "__main__":
    print(reverse_words('hi there how are you'))