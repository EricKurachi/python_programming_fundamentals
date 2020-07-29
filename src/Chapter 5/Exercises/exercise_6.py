"""
Write a function called isPalindrome that returns True if a string given to it is
a palindrome.
"""

def is_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    return False

if __name__ == "__main__":
    print(is_palindrome('radar'))