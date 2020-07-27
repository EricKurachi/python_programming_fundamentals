"""
Write a program that contains a drawTruck function that given an x,y coordinate
on the screen draws a truck using Turtle graphics.
"""

import turtle

def draw_truck_upper_part(car_length, car_color, t):
    t.color('black', car_color)
    t.begin_fill()
    # bottom
    t.forward(car_length)  
    # bumper
    t.left(90)
    t.forward(50)   
    # hood
    t.left(90)
    t.forward(40)   
    # roof
    t.right(45)
    t.forward(70)
    t.left(45)
    t.forward(40)
    t.left(90)
    t.forward(45)   
    # tail
    t.right(90)
    t.forward(120)  
    # rear bumper
    t.left(90)
    t.forward(55)  
    # end 
    t.left(90)
    t.end_fill()

def draw_wheels(car_length, wheel_radius, wheel_color, t):
    t.color(wheel_color, wheel_color)
    # get in first wheel position
    t.penup()
    t.forward(car_length/4)
    t.right(180)
    t.pendown()
    # draw first wheel
    t.begin_fill()
    t.circle(wheel_radius)
    t.end_fill()
    # get in second wheel position
    t.right(180)
    t.penup()
    t.forward(car_length/2)
    t.pendown()
    t.right(180)
    # draw second wheel
    t.begin_fill()
    t.circle(wheel_radius)
    t.end_fill()


def draw_truck(x, y, car_length, wheel_radius, car_color, wheel_color, t): 
    t.penup()
    t.goto(x, y)
    t.pendown()

    draw_truck_upper_part(car_length, car_color, t)
    draw_wheels(car_length,wheel_radius, wheel_color, t)


def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    draw_truck(40, 200, 250, 30, 'gray', 'black', t)
    screen.exitonclick()

if __name__ == "__main__":
    main()