"""
Write a short program that asks the user to enter a month and
prints a message depending on the month entered according to the messages
in Fig.2.6. Then use the step into and over ability of the debugger to examine
the code to see what happens.
"""

chosen_month = input("Please enter a month: ")

if chosen_month == "January":
    print("Hello Snow!")
elif chosen_month == "February":
    print("More Snow!")
elif chosen_month == "March":
    print("No More Snow!")
elif chosen_month == "April":
    print("Almost Golf Time")
elif chosen_month == "May":
    print("Time to Golf")
elif chosen_month == "June":
    print("School’s Out")
elif chosen_month == "July":
    print("Happy Fourth")
elif chosen_month == "August":
    print("Still Golfing")
elif chosen_month == "September":
    print("Welcome Back!")
elif chosen_month == "October":
    print("Fall Colors")
elif chosen_month == "November":
    print("Turkey Day")
elif chosen_month == "December":
    print("Merry Christmas!")
else:
    print("You entered an invalid month")

