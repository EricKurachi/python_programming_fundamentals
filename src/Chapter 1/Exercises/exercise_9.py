"""
Complete the program started in Practices Problem 1.10. Write a program that
asks the user to enter the two legs of a right triangle. The program should print
the length of the hypotenuse. If sideA and sideB are the lengths of the two legs
and sideC is the length of the third leg of a right triangle, then the Pythagorean
theorem says that sideA2 + sideB2 = sideC2. Ask the user to enter sideA and
sideB. Your program should print the value of sideC.
Please enter the length of the first leg: 3
Please enter the length of the second leg: 4
The length of the hypotenuse is 5.0
"""

side_a = float(input("Please enter the length of the first leg: "))
side_b = float(input("Please enter the length of the second leg: "))

side_c = (side_a ** 2 + side_b ** 2) ** 0.5

print("The length of the hypotenuse is {}".format(side_c))
