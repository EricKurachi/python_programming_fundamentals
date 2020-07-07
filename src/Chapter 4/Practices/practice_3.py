"""
Use the turtle module to write a program that draws a 4WD truck.
"""

import turtle as t

screen = t.getscreen()
wheel_radius = 30
car_length = 250

t.color('black', 'gray')
t.begin_fill()
t.forward(car_length)  # bottom
t.left(90)
t.forward(50)   # bumper
t.left(90)
t.forward(40)   # hood
t.right(45)
t.forward(70)
t.left(45)
t.forward(40)
t.left(90)
t.forward(45)   # roof
t.right(90)
t.forward(120)  # tail
t.left(90)
t.forward(55)   # rear bumper
t.end_fill()

t.penup()
t.left(90)
t.forward(car_length/4)
t.right(180)
t.pendown()
t.color('black', 'black')

# Draw wheels
t.begin_fill()
t.circle(wheel_radius)
t.end_fill()
t.right(180)
t.penup()
t.forward(car_length/2)
t.pendown()
t.right(180)
t.begin_fill()
t.circle(wheel_radius)
t.end_fill()


screen.exitonclick()
