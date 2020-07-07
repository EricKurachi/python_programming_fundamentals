"""
How would you create a second Turtle object for r if that’s really
what you wanted?
"""
import turtle


t = turtle.Turtle()
screen = t.getscreen()
t.forward(50)

r = turtle.Turtle()

r.left(90)
r.forward(100)

t.left(90)
t.forward(50)

screen.exitonclick()
