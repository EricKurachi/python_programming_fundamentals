"""
Write a program that plots the function
g(x) = x4/4 − x3/3 − 3x2
"""

import turtle

t = turtle.Turtle()
t.speed('fastest')
screen = t.getscreen()
turtle.setworldcoordinates(-20, -20, 20, 20)

# axis
t.goto(25, 0)
t.goto(-25, 0)
t.goto(0, 0)
t.goto(0, 25)
t.goto(0, -25)

# plot
t.color('red')
t.penup()
x = -4
t.goto(x, (x ** 4 / 4) - (x ** 3 / 3) - (3 * x ** 2))
t.pendown()
while x < 6:
    t.goto(x, (x ** 4 / 4) - (x ** 3 / 3) - (3 * x ** 2))
    x += 0.01

screen.exitonclick()
