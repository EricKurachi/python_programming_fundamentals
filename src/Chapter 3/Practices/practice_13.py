"""
Write a program that asks the user to enter an integer and computes the factorial of that integer, usually written n!
in mathematics. The definition of factorial says that 0! = 1 and for n > 0, n! = 1 ∗ 2 ∗ 3 ... ∗ n.
"""

n = int(input("Enter the n of n!: "))
fact = 1

for i in range(n):
    fact *= i + 1

print(fact)