"""
You can keep track of your car’s miles per gallon if you keep track of how many
miles you drive your car on a tank of gas and you always fill up your tank when
getting gas. Write a program that asks the user to enter the number of miles you
drove your car and the number of gallons of gas you put in your car and then
prints the miles per gallon you got on that tank of gas. Here is a sample run of
the program.
Please enter the miles you drove : 256
Please enter the gallons of gas you put in the tank : 10.1
You got 25.346534653465348 mpg on that tank of gas.
"""

miles_drove = float(input("Please enter the miles you drove: "))
gallons = float(input("Please enter the gallons of gas you put in the tank: "))

print("You got {} mpg on that tank of gas.".format(miles_drove/gallons))
