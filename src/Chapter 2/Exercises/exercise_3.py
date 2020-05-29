"""
Write a program that converts centimeters to yards, feet, and inches. There are
2.54 cm in an inch. You can solve this problem by doing division, multiplication,
addition, and subtraction. Converting a float to an int at the appropriate time will
help in solving this problem. When you run the program it should look exactly
like this (except possibly for decimal places in the inches):
How many centimeters do you want to convert ? 127.25
This is 1 yard , 1 foot , 2.098425 inches .
This is a modification of the program in Exercise 5 of Chap.1. In this version of
it you should print “yard” when there is one yard, and “yards” when there is more
than one yard. If there are zero yards then it should not print “yard” or “yards”.
The same thing applies to “feet”. Use an if statement to determine the label to
print and if the label should be printed at all.
"""

centimeters = float(input("How many centimeters do you want to convert? "))

if centimeters < 0:
    print("Invalid value")
    exit(0)

to_yards = int(centimeters * 0.0109361)
to_feet = int(centimeters * 0.0328084)
to_inches = int(centimeters * 0.3937007874)

if to_yards > 1:
    yard_str = "yards,"
elif to_yards == 1:
    yard_str = "yard,"
else:
    yard_str = ""

if to_feet > 1:
    feet_str = "feet,"
elif to_feet == 1:
    feet_str = "foot,"
else:
    feet_str = ""

if to_yards > 0:
    print("this is", to_yards, yard_str, to_feet, feet_str, to_inches, "inches.")
elif to_feet > 0:
    print("this is", to_feet, feet_str, to_inches, "inches.")
else:
    print("this is", to_inches, "inches.")