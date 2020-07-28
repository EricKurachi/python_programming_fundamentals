"""
Modify the program in the previous exercise to add a scale parameter to the
drawTruck function.
"""

import turtle

def draw_truck_upper_part(car_length, car_color, scale, t):
    t.color('black', car_color)
    t.begin_fill()
    # bottom
    t.forward(car_length * scale)  
    # bumper
    t.left(90)
    t.forward(50 * scale)   
    # hood
    t.left(90)
    t.forward(40 * scale)   
    # roof
    t.right(45)
    t.forward(70 * scale)
    t.left(45)
    t.forward(40 * scale)
    t.left(90)
    t.forward(45 * scale)   
    # tail
    t.right(90)
    t.forward(120 * scale)  
    # rear bumper
    t.left(90)
    t.forward(55 * scale)  
    # end 
    t.left(90)
    t.end_fill()

def draw_wheels(car_length, wheel_radius, wheel_color, scale, t):
    t.color(wheel_color, wheel_color)
    # get in first wheel position
    t.penup()
    t.forward(car_length/4 * scale)
    t.right(180)
    t.pendown()
    # draw first wheel
    t.begin_fill()
    t.circle(wheel_radius * scale)
    t.end_fill()
    # get in second wheel position
    t.right(180)
    t.penup()
    t.forward(car_length/2 * scale)
    t.pendown()
    t.right(180)
    # draw second wheel
    t.begin_fill()
    t.circle(wheel_radius * scale)
    t.end_fill()


def draw_truck(x, y, car_color, wheel_color, scale, t, car_length=250, wheel_radius=30): 
    t.penup()
    t.goto(x, y)
    t.pendown()

    draw_truck_upper_part(car_length, car_color, scale, t)
    draw_wheels(car_length,wheel_radius, wheel_color, scale, t)


def main():
    t_1 = turtle.Turtle()
    t_2 = turtle.Turtle()
    t_3 = turtle.Turtle()
    screen = t_1.getscreen()
    draw_truck(50, -100, 'red', 'blue', 1.3, t_1)
    draw_truck(-200, -200, 'gray', 'black', 1.5, t_2)
    draw_truck(40, 200, 'green', 'black', 1, t_3)
    screen.exitonclick()

if __name__ == "__main__":
    main()