"""
Set a break point on the print(c) line. Run it with the debugger and watch it as it runs. Then answer these questions:
1. Does the string s change as the code is executed?
2. What happens if the user just presses enter when prompted instead of typing any characters?
"""

s = input("Please type some characters and press enter: ")
for c in s:
    print(c)
print("Done")

# The string s doesn't change
# The for loop is not activated
