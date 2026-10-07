from turtle import Turtle, Screen

cumali = Turtle()
screen = Screen()

def move_forward():
    cumali.forward(10)

def move_backward():
    cumali.backward(10)

def move_left():
    new_heading = cumali.heading() + 10
    cumali.setheading(new_heading)

def move_right():
    new_heading = cumali.heading() - 10
    cumali.setheading(new_heading)

def reset():
    cumali.clear()
    cumali.penup()
    cumali.home()
    cumali.pendown()

screen.listen()
screen.onkey(key= "w" , fun= move_forward)
screen.onkey(key= "s" , fun= move_backward)
screen.onkeypress(key= "a" , fun= move_left)
screen.onkeypress(key= "d" , fun = move_right)
screen.onkey(key= "c" , fun= reset)

screen.exitonclick()