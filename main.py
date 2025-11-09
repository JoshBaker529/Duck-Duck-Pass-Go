from flask import Flask, render_template
import getPos
import lat_long
import turtle
import random

app = Flask(__name__)

point = 0
duck = turtle.Turtle()


POINTS_X= 280
POINTS_Y= -250
target = turtle.Turtle()
def duck_location(x, y):
    duck.shape("duck-dance.gif")
    print(duck.shapesize())
    duck.penup()
    duck.goto(x, y)
    screen.update()

def button_clicked(x, y):
    left = BUTTON_X
    right = BUTTON_X + 100
    bottom = BUTTON_Y
    top = BUTTON_Y + 50

    if left <= x <= right and bottom <= y <= top:
        print("Button Clicked")
        #ADD ACTION HERE
        if (target.pos()[0]-25 <= duck.pos()[0] <= target.pos()[0]+25 and target.pos()[1]-25 <= duck.pos()[1] <= target.pos()[1]+25):

            print("Points get!")
            global point
            point += 200
            print(point)
            points.clear()
            points.penup()
            points.goto(POINTS_X,POINTS_Y)
            points.pendown()
            points.begin_fill()
            points.fillcolor("blue")
            points.forward(100)
            points.left(90)
            points.forward(50)
            points.left(90)
            points.forward(100)
            points.left(90)
            points.forward(50)
            points.left(90)
            points.end_fill()
            points.hideturtle()
            points.write(point, align="left", font=("Arial", 16, "bold"))
            mov_goal()
        screen.bgcolor("lightgreen")
    else:
        duck_location(x, y)


WIDTH = 900
HEIGHT = 582

BUTTON_X = -410
BUTTON_Y = -250

#creating the screen
screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgpic("thumbnail_map_bigger.gif")
screen.title("Duck Duck Pass Go")
screen.addshape("duck-dance.gif")
screen.tracer(0)

button = turtle.Turtle()
button.penup()
button.goto(BUTTON_X, BUTTON_Y)
button.pendown()
button.begin_fill()
button.fillcolor("lightblue")
button.forward(100)
button.left(90)
button.forward(50)
button.left(90)
button.forward(100)
button.left(90)
button.forward(50)
button.end_fill()
button.hideturtle()
button.write("                       PASS GO!!", align="center", font=("Arial", 16, "bold"))
screen.update()


points = turtle.Turtle()
points.penup()
points.goto(POINTS_X,POINTS_Y)
points.pendown()
points.begin_fill()
points.fillcolor("blue")
points.forward(100)
points.left(90)
points.forward(50)
points.left(90)
points.forward(100)
points.left(90)
points.forward(50)
points.left(90)
points.end_fill()
points.hideturtle()
points.write(point, align="left", font=("Arial", 16, "bold"))
screen.update()

target.shape("turtle")
target.color("yellow")
target.penup()
def mov_goal():
    xcoord = random.randint(-WIDTH // 2, WIDTH // 2)
    ycoord = random.randint(-HEIGHT // 2, HEIGHT // 2)
    target.goto(xcoord, ycoord)

duck_location(200, 200)
# mov_goal()
screen.onclick(button_clicked)

#keep window open until closed manually
screen.mainloop()
