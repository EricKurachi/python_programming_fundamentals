"""
Modify the program from practice Problem 2.1 to print “Merry
Christmas!” if the month is December and “You’ll have to wait” otherwise. It
should still print “Have a Happy New Year!” in either case as the last line of
output. Then run the program at least twice using step into and over to see how
it behaves when “December” is entered and how the program behaves when
anything else is entered.
"""

chosen_month = input("please enter the name of a month: ")

if chosen_month == "December":
    print("Merry Christmas!")
else:
    print("You’ll have to wait")

print("Have a Happy New Year!")
