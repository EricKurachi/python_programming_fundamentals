import datetime
import turtle

auto_data = []

with open("csv\\Toyota4Runner.csv") as f:
    header = f.readline().rstrip()
    eof = False
    while not eof:
        line = eval(f.readline().rstrip())
        if line[0] != '':
            auto_data.append(line)
        else:
            eof = True

auto_turtle = turtle.Turtle()
screen = auto_turtle.getscreen()
screen.setworldcoordinates(0, 0, 25, 25)

date_nxt = datetime.datetime.strptime(auto_data[0][2] + ' ' + auto_data[0][3], "%Y-%m-%d %I:%M %p")
time = 0

x_sum = 0
y_sum = 0
x_square_sum = 0
x_y_sum = 0
n = 0

for line in auto_data:
    n += 1
    if line[0] == "Gas":
        date_ant = date_nxt
        date_nxt = datetime.datetime.strptime(line[2] + ' ' + line[3], "%Y-%m-%d %I:%M %p")
        time = float((date_ant - date_nxt).total_seconds())/(3600*24)

        x_sum += time
        y_sum += float(line[1])
        x_square_sum += time ** 2
        x_y_sum += time * float(line[1]) 

        auto_turtle.penup()
        auto_turtle.goto(time, float(line[1]))
        auto_turtle.pendown()
        auto_turtle.dot(20, 'blue')

m = (x_sum * y_sum - n * (x_sum/n) * (y_sum/n))/(x_square_sum - n * (x_sum/n) ** 2)
y_1 = (y_sum/n) + m * (0 - x_sum)
y_2 = (y_sum/n) + m * (30 - x_sum)

auto_turtle.penup()
auto_turtle.goto(0, y_1)
auto_turtle.pendown()
auto_turtle.goto(30, y_2)

print(y_1, y_2)

screen.exitonclick()
