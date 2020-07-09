import xml.etree.ElementTree as ET
import turtle

# import xml doc
tree = ET.parse("xml\\flowerandbg.xml")
root = tree.getroot()
# get all commands
commandList = []
# create all attribute lists
xList = []
yList = []
widthList = []
colorList = []
radiusList = []
attributeList = [xList, yList, widthList, colorList, radiusList]
attributes = ["x", "y", "width", "color", "radius"]
# get all commands with attributes
for command in root.iter('Command'):
    commandList.append(command.text)
    for i in range(len(attributes)):
        attr = command.attrib
        key = attributes[i]
        if key in attr:
            attributeList[i].append(attr[key])
        else:
            attributeList[i].append('NaN')

# input scale factor
scale_factor = float(input('Please enter a scale factor:'))
xList = [float(x) * scale_factor for x in xList]
yList = [float(y) * scale_factor for y in yList]
widthList = [float(width) * scale_factor for width in widthList]
radiusList = [float(radius) * scale_factor for radius in radiusList]

t = turtle.Turtle()
screen = t.getscreen()
screen.colormode(255)
screen.tracer(0)
for i in range(len(commandList)):
    command = commandList[i]
    if command == "PenUp":
        t.penup()
    elif command == "PenDown":
        t.pendown()
    elif command == "GoTo":
        x = float(xList[i])
        y = float(yList[i])
        width = float(widthList[i])
        color = colorList[i]
        t.width(width)
        t.color(color)
        t.goto(x, y)
    elif command == "Circle":
        radius = float(radiusList[i])
        width = float(widthList[i])
        color = colorList[i]
        t.width(width)
        t.pencolor(color)
        t.circle(radius)
    elif command == "BeginFill":
        color = colorList[i]
        t.fillcolor(color)
        t.begin_fill()
    elif command == "EndFill":
        t.end_fill()
    else:
        print("Unknown Command:", command)

count = 0
# create the file structure
for command in root.iter('Command'):
    if commandList[count] == 'GoTo':
        command.set('x', str(xList[count]))
        command.set('y', str(yList[count]))
        command.set('width', str(widthList[count]))
    elif commandList[count] == 'Circle':
        command.set('radius', str(radiusList[count]))
        command.set('width', str(widthList[count]))
    else:
        pass
    count += 1

newFile = input("Please enter the name of the save file: ")
tree.write('xml\\' + newFile + '.xml')

screen.update()
screen.exitonclick()

