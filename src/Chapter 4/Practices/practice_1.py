"""
Write some code that uses a for loop to draw a square using the
turtle module.
"""

import turtle

t = turtle.Turtle()
screen = t.getscreen()
for i in range(4):
    t.forward(100)
    t.left(90)

screen.exitonclick()
