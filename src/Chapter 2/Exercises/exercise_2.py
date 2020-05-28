"""
Write a program that prints a user’s grade given a percent of points achieved in
the class. The program should prompt the user to enter his/her percent of points.
It should then print a letter grade A, A−, B+, B, B−, C+, C, C−, D+, D, D−, F.
The grading scale is given in Fig. 2.11. Use exception handling to check the input
from the user to be sure it is valid. Running the program should look like this:
Please enter your percentage achieved in the class : 92.32
You earned an A - in the class .
"""

try:
    percentage = float(input("Please enter your percentage achieved in the class: "))
except ValueError:
    print("You entered an invalid number")
    exit(0)

if percentage < 0 or percentage > 100:
    print("The percentage must be between 0 and 100")
    exit(0)

grade = "F"

if percentage >= 93.33:
    grade = "A"
elif percentage >= 90:
    grade = "A-"
elif percentage >= 86.67:
    grade = "B+"
elif percentage >= 83.33:
    grade = "B"
elif percentage >= 80:
    grade = "B-"
elif percentage >= 76.67:
    grade = "C+"
elif percentage >= 73.33:
    grade = "C"
elif percentage >= 70:
    grade = "C-"
elif percentage >= 66.67:
    grade = "D+"
elif percentage >= 63.33:
    grade = "D"
elif percentage >= 60:
    grade = "D-"
else:
    grade = "F"

print(grade)
