import turtle as t
import random

turtule = t.Turtle()
t.shape("square")
t.color("blue")
t.colormode(255)

def random_colors():
    r = random.randint(0 , 255)
    b = random.randint(0 , 255)
    g = random.randint(0 , 255)
    color = (r ,g , b)
    return color
directions = [0 , 90 , 180 , 270]

t.pensize(15)
t.speed(8)
for i in range(200):
    t.forward(30)
    t.setheading(random.choice(directions))
    t.color(random_colors())
    

screen = t.Screen()
screen.exitonclick()

