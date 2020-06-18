"""
Write a short program that asks the user to enter the name of
a month. If the user enters “December” your program should print “Merry
Christmas!”. No matter what you enter, your program should print “Have a
Happy New Year!” just before the program terminates. Then, use Step Into and
Step Over to execute each statement that you wrote. Run your program at least
twice to see how it behaves when you enter “December” and how it behaves
when you enter something else.
"""

chosen_month = input("please enter a month: ")

if chosen_month == "December":
    print("Merry Christmas!")

print("Have a Happy New Year!")
