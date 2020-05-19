"""
Write a program that asks the user to enter their name. Then it should print out the
ASCII equivalent of each of the first four characters of your name. For instance,
here is a sample run of the program below.
Please enter your name : Kent
K ASCII value is 75
e ASCII value is 101
n ASCII value is 110
t ASCII value is 116
"""
name = ''

# the while line ensures that the string have at least 4 characters, but for the exercise it's optional
while len(name) < 4:
    name = input("Please enter your name: ")

print("{} ASCII value is {}".format(name[0], ord(name[0])))
print("{} ASCII value is {}".format(name[1], ord(name[1])))
print("{} ASCII value is {}".format(name[2], ord(name[2])))
print("{} ASCII value is {}".format(name[3], ord(name[3])))
