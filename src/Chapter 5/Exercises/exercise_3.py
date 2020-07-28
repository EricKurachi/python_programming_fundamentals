"""
Write a program that contains a function called drawRegularPolygon where you
give it a Turtle, the number of sides of the polygon, and the side length and it
draws the polygon for you
"""

import turtle

def draw_regular_polygon(t, n_sides, side_length):
    i = 0
    while i < n_sides:
        t.forward(side_length)
        t.left(360/n_sides)
        i += 1

def main():
    t_1 = turtle.Turtle()
    t_2 = turtle.Turtle()
    t_3 = turtle.Turtle()
    screen = t_1.getscreen()
    draw_regular_polygon(t_1, 3, 30)
    draw_regular_polygon(t_2, 5, 60)
    draw_regular_polygon(t_3, 8, 40)
    screen.exitonclick()

if __name__ == "__main__":
    main()