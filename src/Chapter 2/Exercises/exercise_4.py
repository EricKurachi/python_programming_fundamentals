"""
Write a program that computes the minimum number of bills and coins needed
to make change for a person. For instance, if you need to give $34.36 in change
you would need one twenty, one ten, four ones, a quarter, a dime, and a penny.
You don’t have to compute change for bills greater than $20 dollar bills or for
fifty cent pieces. You can solve this problem by doing division, multiplication,
subtraction, and converting floats to ints when appropriate. So, when you run the
program it should look exactly like this:
How much did the item cost : 65.64
How much did the person give you: 100.00
The person ’s change is $34 .36
The bills or the change should be:
1 twenty
1 ten
4 ones
1 quarter
1 dime
1 penny
"""
try:
    cost = float(input('How much did the item cost: '))
    pay = float(input('How much did the person give you: '))
except ValueError:
    print("Invalid value")
    exit(0)

change = pay - cost

if change < 0:
    print("insuficient money")
    exit(0)

print("The person's change is ${0:.2f}".format(pay-cost))
print("The bills or the change should be:")

quantity = int(change / 20)
if quantity == 1:
    print("{} twenty".format(quantity))
elif quantity > 1:
    print("{} twenties".format(quantity))
change %= 20

quantity = int(change / 10)
if quantity > 0:
    print("{} ten".format(quantity))
    change %= 10

quantity = int(change / 5)
if quantity > 0:
    print("{} five".format(quantity))
    change %= 5

quantity = int(change % 5)
if quantity == 1:
    print("{} one".format(quantity))
elif quantity > 1:
    print("{} ones".format(quantity))
change %= 1

quantity = int(change / 0.25)
if quantity == 1:
    print("{} quarter".format(quantity))
elif quantity > 1:
    print("{} quarters".format(quantity))
change %= 0.25

quantity = int(change/0.1)
if quantity == 1:
    print("{} dime".format(quantity))
elif quantity > 1:
    print("{} dimes".format(quantity))
change %= 0.1

quantity = int(change/0.05)
if quantity > 0:
    print("{} nickel".format(quantity))
    change %= 0.05

quantity = change * 100
if quantity == 1:
    print("{0:.0f} penny".format(change*100))
elif quantity > 1:
    print("{0:.0f} pennies".format(change * 100))
