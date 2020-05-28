"""
Type in the code of Example 2.6. Execute the code using a debugger like the one
included with the Wing IDE 101. Step into and over the code using the debugger.
Enter a menu choice of 1. Using the line numbers in Example 2.6, which lines of
the program are executed when you enter a 1 for the menu choice. List these lines.
Do the same for each of the other menu choice values. If you run the program and
enter a menu choice of 5, which lines of the program are executed. If you use the
debugger to answer this question you will be guaranteed to get it right and you’ll
learn a little about using a debugger.
"""

x = float(input(" Please enter a number :"))
y = float(input(" Please enter a second number :"))

print(" 1) Add the two numbers ")
print(" 2) Subtract the two numbers ")
print(" 3) Multiply the two numbers ")
print(" 4) Divide the two numbers ")

choice = int(input(" Please enter your choice :"))

print(" The answer is :", end="")

if choice == 1:
    print(x + y)
elif choice == 2:
    print(x - y)
elif choice == 3:
    print(x * y)
elif choice == 4:
    print(x / y)
else:
    print(" You did not enter a valid choice .")
