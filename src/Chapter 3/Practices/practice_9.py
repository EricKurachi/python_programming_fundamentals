"""
What would happen if the if contains_even statement were indented under the for loop?
# It will print the result for each element of the list
"""

s = input("Please enter a list of integers: ")
lst = s.split()  # Now lst is a list of strings.

# make a guess first
contains_even = False

# the iterate over the list
for element in lst:
    x = int(element)
    # check your guess in the loop
    # and fix it if needed
    if x % 2 == 0:
        contains_even = True

# after the loop you know whether
# your guess was correct or not.
if contains_even:
    print("The list contained an even number")
else:
    print("The list did not contain an even number")


