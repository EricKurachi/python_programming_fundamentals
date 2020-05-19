"""
Write a short program that computes the length of the
hypotenuse of a right triangle given the two legs.
The program should use three variables, sideA, sideB, and sideC. The
Pythagorean theorem states that the sum of the squares of the two legs of
the triangle equals the square of the hypotenuse. Be sure to assign all three
variables their correct values and print the length of sideC at the end of the
program. HINT: Raising a value to the 1/2 power is the same thing as finding
the square root. Try values 6 and 8 for sideA and sideB
"""

side_a = 6
side_b = 8

side_c = (side_a ** 2 + side_b ** 2) ** (0.5)

print(side_c)

