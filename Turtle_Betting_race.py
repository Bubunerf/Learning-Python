from turtle import Turtle , Screen
import random



is_race_on = False

screen = Screen()
screen.setup(width= 500 ,height= 400)

user_bet = screen.textinput(title= "Make your bet" , prompt= "Which turtle will win the race? Enter a color: ")

all_turtles = []

def racing_turtles():
    colors = ["red" , "blue" , "purple" , "green" , "yellow" , "orange"]

    pos_x = -230
    pos_y = -100

    for i in range(len(colors)):
        new_turtle = Turtle(shape= "turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(x= pos_x , y =pos_y)
        new_turtle.pendown()
        pos_y += 40
        all_turtles.append(new_turtle)   

racing_turtles()

if user_bet:
    is_race_on = True

while is_race_on:
    for i in all_turtles:
        if i.xcor() > 230:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print(f"You Win!, the winnning color was {winning_color}")
            else:
                print(f"You Lose the winning color is {winning_color}")
            
        rand_num = random.randint(0 , 5)
        i.penup()
        i.forward(rand_num)
        
        

    

    





screen.exitonclick()