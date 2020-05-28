"""
In Minnesota you can fish if you are 15 years old or less and your
parent has a license. If you are 16 years old or more you need to have your
own license. Write a program that uses short circuit logic to tell someone if
they are legal to fish in Minnesota. First ask them how old they are, whether
they have a license or not, and whether their parent has a license or not.
"""

age = int(input("Please enter your age: "))
own_license = input("Do you have a license?: ")
parent_license = input("Do your parent have a license?: ")

if (age <= 15 and parent_license == 'yes') or (age > 15 and own_license == 'yes'):
    print("You are legal to fish in Minnesota")
else:
    print("You are not legal to fish in Minnesota")
