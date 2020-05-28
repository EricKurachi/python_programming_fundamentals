"""
Use the guess and check pattern to determine if a triangle is a
perfect triangle. A perfect triangle has side lengths that are multiples of 3, 4
and 5. Ask the user to enter the shortest, middle, and longest sides of a triangle
and then print “It is a perfect triangle “if it is and “It is not a perfect triangle”
if it isn’t. You may assume that the side lengths are integers. Let your guess be
that the message you will print is “It is a perfect triangle”.
"""

side_a = int(input("Please insert the lenght of the shortest side: "))
side_b = int(input("Please insert the lenght of the middle side: "))
side_c = int(input("Please insert the lenght of the longest side: "))

result = "It is a perfect triangle"

if (side_a % 3) != 0:
    result = "It is not a perfect triangle"
if (side_b % 4) != 0:
    result = "It is not a perfect triangle"
if (side_c % 5) != 0:
    result = "It is not a perfect triangle"

print(result)
