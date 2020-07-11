import random
import turtle

rand = random.Random()
t = turtle.Turtle()
screen = t.getscreen()
wheel_radius = 30
car_length = 250

t.penup()
initial_x = rand.randint(-400, 400)
initial_y = rand.randint(-400, 400)
t.goto(initial_x, initial_y)
t.pendown()

scale = rand.random()

t.color('black', 'gray')
t.begin_fill()
t.forward(car_length*scale)  # bottom
t.left(90)
t.forward(50*scale)   # bumper
t.left(90)
t.forward(40*scale)   # hood
t.right(45)
t.forward(70*scale)
t.left(45)
t.forward(40*scale)
t.left(90)
t.forward(45*scale)   # roof
t.right(90)
t.forward(120*scale)  # tail
t.left(90)
t.forward(55*scale)   # rear bumper
t.end_fill()

t.penup()
t.left(90)
t.forward(car_length/4*scale)
t.right(180)
t.pendown()
t.color('black', 'black')

# Draw wheels
t.begin_fill()
t.circle(wheel_radius*scale)
t.end_fill()
t.right(180)
t.penup()
t.forward(car_length/2*scale)
t.pendown()
t.right(180)
t.begin_fill()
t.circle(wheel_radius*scale)
t.end_fill()


screen.exitonclick()
