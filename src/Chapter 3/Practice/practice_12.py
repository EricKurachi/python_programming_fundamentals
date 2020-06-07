"""
Modify the code in Example 3.11 to count the number of even
integers entered by the user.
"""

s = input("Please enter a list of integers: ")
lst = s.split()  # Now lst is a list of strings.
count = 0  # Here is the beginning of the accumulator pattern
for e in lst:
    if int(e) % 2 == 0:
        count = count + 1

print("There were", count, "even integers in the list.")
