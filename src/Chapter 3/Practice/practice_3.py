"""
write a program that asks the user to enter “yes” or “no”. If they enter “yes” then you should print “You entered yes”.
and likewise if they enter “no”. However, make sure you accept “Yes”, “yEs”, or any other combination of upper and lower
case letters for “yes” and for “no”.
"""

s = input("Please enter 'yes' or 'no': ")
s = s.lower()

if s == 'yes':
    print('You entered yes')
else:
    print('You entered no')
