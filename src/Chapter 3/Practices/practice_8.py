"""
You can see what the split method does by setting some variable to the result of s.split(). For instance,
the second line could be: splitWords = s. split() Modify the code to add this line and use splitWords in the for loop.
"""
s = input("Please type some characters and press enter:")
split_words = s.split()
for word in split_words:
    print(word)
print("Done")

# method .split() returns a list with the words of the string
# the for loop iterates over the list elements
