"""
Modify the code in Example 3.4 to print the characters to the screen as capital letters whether the user enters capital
letters or not with one letter on each line.
"""

s = input("Please type some characters and press enter: ")
s = s.upper()
for c in s:
    print(c)
print("Done")
