"""
Add exception handling to the program in practice Problem 2.6
so that if the user answers something other than their age that the program
prints “You did not enter your age correctly”.
"""

try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("You did not enter your age correctly")
    exit(0)

own_license = input("Do you have a fishing license (yes/no)?: ")
parent_license = input("Do your parent have a fishing license (yes/no)?: ")

if (age < 16 and parent_license == 'yes') or own_license == 'yes':
    print("You are legal to fish in Minnesota")
else:
    print("You are not legal to fish in Minnesota")
