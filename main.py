import turtle
from turtle import Turtle, Screen
from random import random
from random import randint
turtle.colormode(255)
def colour():
    a = randint(0, 255)
    b = randint(0, 255)
    c = randint(0, 255)
    return (a, b, c)

my = Turtle()
my.speed(0)
for val in range(40):
 my.color(colour())
 my.circle(100)
 my.left(10)


# turtle.colormode(255)
# def colour():
#     a = random.randint(0, 255)
#     b = random.randint(0, 255)
#     c = random.randint(0, 255)
#     return (a, b, c)
# my = Turtle()
# my.hideturtle()
# def forward():
#     my.forward(randint(0,30))
# def turn_right():
#     my.right(90)
#     my.forward(randint(0, 30))
# def turn_left():
#     my.left(90)
#     my.forward(randint(0, 30))
# def go_back():
#     my.backward(randint(0,30))
# list = [forward, turn_left, turn_right, go_back ]
# a = False
# my.speed("fast")
# my.width(15)
# while a is False:
#  my.color(colour())
#  random.choice(list)()
#






# my.up()
# my.sety(100)
# my.down()
# def draw(sides):
#     for val in range(sides):
#         my.forward(100)
#         my.right(angle)
# for val in range (3 , 11):
#     angle = 360 / val
#     my.color(choice(colour_list))
#     draw(val)
# my_baby.forward(100)
# my_baby.left(90)
# my_baby.forward(100)
# my_baby.left(90)
# my_baby.forward(100)
# for _ in range(25):
#     my.forward(5)
#     my.up()
#     my.forward(5)
#     my.down()
screen = Screen()
screen.exitonclick()




