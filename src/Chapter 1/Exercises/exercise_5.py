"""
Write a program that converts centimeters to yards, feet, and inches. There are
2.54 cm in an inch. You can solve this problem by doing division, multiplication,
addition, and subtraction. Converting a float to an int at the appropriate time will
help in solving this problem. When you run the program it should look exactly
like this (except possibly for decimal places in the inches):
How many centimeters do you want to convert? 127.25
This is 1 yards , 1 feet , 2.098425 inches .
"""

centimeters = float(input("How many centimeters do you want to convert? "))

to_yards = centimeters * 0.0109361
to_feet = centimeters * 0.0328084
to_inches = centimeters * 0.3937007874

print("this is {} yards, {} feet, {} inches.".format(to_yards, to_feet, to_inches))
