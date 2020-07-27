"""
Write a program that contains a drawTruck function that given an x,y coordinate
on the screen draws a truck using Turtle graphics.
"""

import turtle

def drawTruck(x, y, t): 
    t.penup()
    t.goto(x, y)
    t.pendown()

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


def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    drawTruck(40, 200, t)
    screen.exitonclick()

if __name__ == "__main__":
    main()