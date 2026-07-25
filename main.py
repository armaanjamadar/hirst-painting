from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()
screen.colormode(255)

colors = ["red", "blue", "green", "purple", "orange", "magenta", "cyan", "violet", "indigo", "yellow", "grey"]

turtle.penup()
turtle.hideturtle()
x_axis = -230
y_axis = -220
turtle.goto(x_axis, y_axis)

for _ in range(10):
    for _ in range(10):
        turtle.dot(20, random.choice(colors))
        turtle.forward(50)
    y_axis += 50
    turtle.goto(x_axis, y_axis)



screen.exitonclick()