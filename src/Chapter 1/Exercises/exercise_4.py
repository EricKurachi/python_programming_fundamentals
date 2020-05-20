"""
Write a program that converts US Dollars to a Foreign Currency. You can do this
by finding the exchange rate on the internet and then prompting for the exchange
rate in your program. When you run the program it should look exactly like this:
What is the amount of US Dollars you wish to convert ? 31.67
What is the current exchange rate? 0.9825
The amount in the Foreign Currency is $31.12
"""

us_value = float(input("What is the amount of US Dollars you wish to convert? "))
exchange_rate = float(input("What is the current exchange rate? "))

print("The amount in the Foreing Currency is ${0:.2f}".format(us_value * exchange_rate))
