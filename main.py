from flask import Flask, render_template
import turtle

app = Flask(__name__)

def duck_location(x, y):
    duck = turtle.Turtle()
    duck.shape("duck-dance.gif")
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
        screen.bgcolor("lightgreen")


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
button.write("GO!!", align="center", font=("Arial", 16, "bold"))
screen.update()

duck_location(200, 200)

screen.onclick(button_clicked)

#keep window open until closed manually
screen.mainloop()
