from turtle import Turtle , Screen


screen = Screen()
screen.setup(width= 500 ,height= 400)

user_bet = screen.textinput(title= "Make your bet" , prompt= "Which turtle will win the race? Enter a color: ")
print(user_bet)



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
    return new_turtle    


racing_turtles()



screen.exitonclick()