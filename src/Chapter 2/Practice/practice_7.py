"""
Use the guess and check pattern to determine if a triangle is a
perfect triangle. You must allow the user to enter any side length for the three
sides of the triangle, not just integers. A perfect triangle has side lengths that
are multiples of 3, 4 and 5. Ask the user to enter the three side lengths and then
print “It is a perfect triangle” if it is and “It is not a perfect triangle” if it isn’t.
"""

side_a = float(input("please enter the size of the shortest side: "))
side_b = float(input("please enter the size of the medium side: "))
side_c = float(input("please enter the size of the biggest side: "))

ratio = side_a / 3

guess = "It is a perfect triangle"

if abs((ratio - side_b / 4) / side_b) > 0.001:
    guess = "It is not a perfect triangle"
if abs((ratio - side_c / 5) / side_c) > 0.001:
    guess = "It is not a perfect triangle"

print(guess)
