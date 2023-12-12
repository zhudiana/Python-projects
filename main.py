import turtle
from turtle import Turtle, Screen, TK
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win thr race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []

y = -100
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 50
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                TK.messagebox.showinfo(title="Result:", message=f"You've won! The {winning_color} is the winner")
            else:
                TK.messagebox.showinfo(title="Result:", message=f"You've lost! The {winning_color} is the winner")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()