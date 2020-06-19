"""
Write a program that asks the user to enter a list and then builds a new list which
is the reverse of the original list.
"""

given_list = input("Please enter a list: ")

rev = given_list.split()[::-1]

print("The reversed list is", rev)
