"""Write a program that computes the minimum number of bills and coins needed
to make change for a person. For instance, if you need to give $34.36 in change
you would need one twenty, one ten, four ones, a quarter, a dime, and a penny.
You don’t have to compute change for bills greater than $20 dollar bills or for
fifty cent pieces. You can solve this problem by doing division, multiplication,
subtraction, and converting floats to ints when appropriate. So, when you run the
program it should look exactly like this:
How much did the item cost: 65.64
How much did the person give you: 100.00
The person’s change is $34.36
The bills or the change should be:
1 twenties
1 tens
0 fives
4 ones
1 quarters
1 dimes
0 nickels
1 pennies"""

cost = float(input('How much did the item cost: '))
pay = float(input('How much did the person give you: '))
change = pay - cost

print("The person's change is ${0:.2f}".format(pay-cost))
print("The bills or the change should be:")

print("{} twenties".format(int(change/20)))
change %= 20

print("{} tens".format(int(change/10)))
change %= 10

print("{} fives".format(int(change/5)))
change %= 5

print("{} ones".format(int(change % 5)))
change %= 1

print("{} quarters".format(int(change/0.25)))
change %= 0.25

print("{} dimes".format(int(change/0.1)))
change %= 0.1

print("{} nickels".format(int(change/0.05)))

print("{0:.0f} pennies".format(change*100))


