import datetime
import turtle


auto_file = ["csv\\NissanVersa.csv", "csv\\SuzukiS40.csv", "csv\\Toyota4Runner.csv"]
auto_data = []

for i in range(len(auto_file)):
    auto_data.append([])
    with open(auto_file[i]) as f:
        header = f.readline().rstrip()
        eof = False
        while not eof:
            line = eval(f.readline().rstrip())
            if line[0] != '':
                auto_data[i].append(line)
            else:
                eof = True

auto_turtle = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
screen = auto_turtle[0].getscreen()
screen.setworldcoordinates(0, 0, 250, 100)

date_nxt = datetime.datetime.strptime(auto_data[0][0][2], "%Y-%m-%d")
time = 0
for i in range(len(auto_file)):
    for line in auto_data[i]:
        if line[0] == "Gas":
            date_ant = date_nxt
            date_nxt = datetime.datetime.strptime(line[2], "%Y-%m-%d")
            time += float((date_ant - date_nxt).total_seconds())/(3600*24)
            auto_turtle[i].goto(time, float(line[1]))

screen.exitonclick()
