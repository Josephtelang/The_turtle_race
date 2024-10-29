from turtle import Turtle , Screen
from random import choice,randint

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make the bet",prompt="which turtle will win the race ? Enter your colour :")
colour = ["red","blue","green","orange","yellow","purple"]
y_list = [-100,-70,-40,-10,20,50]
all_turtle = []

for turtle_index in range(0,6):
    new_turtle= Turtle(shape="turtle")
    new_turtle.penup()
    colour_of_turtle = choice(colour)
    new_turtle.color(colour_of_turtle)
    new_turtle.goto(x=-240,y=y_list[turtle_index])
    colour.remove(colour_of_turtle)
    all_turtle.append(new_turtle)


if user_bet:
    race_is = True

while race_is:
    for turtle in all_turtle:
        
        if turtle.xcor() > 230:
            race_is = False
            winner_colour = turtle.pencolor()
            if winner_colour == user_bet:
                print(f"You have won !. The {winner_colour} is the winner")
            else:
                print(f"you have lose !. The {winner_colour} is the winner")

        random_num = randint(1,10)
        turtle.forward(random_num)

            




screen.exitonclick()
