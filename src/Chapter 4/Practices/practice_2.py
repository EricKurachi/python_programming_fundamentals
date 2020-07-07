"""
Write a short program that prompts the user to enter the number
of sides of a regular polygon. Then draw a regular polygon with that many
sides.
"""

import turtle as t

screen = t.getscreen()
sides = int(screen.textinput('RPS', 'Please insert the number of sides of the poligon: '))
angle = 360/sides

for i in range(sides):
    t.forward(30)
    t.left(angle)
screen.exitonclick()
