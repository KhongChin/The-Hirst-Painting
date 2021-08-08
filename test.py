from turtle import Screen, Turtle
import random


def left_forward():
    turtle.left(90)
    turtle.forward(30)


def right_forward():
    turtle.right(90)
    turtle.forward(30)


def move_forward():
    turtle.forward(30)


def move_backward():
    turtle.backward(30)


turtle = Turtle()
screen = Screen()
turtle.shape("classic")


# Challenge 3
# for i in range(3, 11):
#     turtle.color(random.random(), random.random(), random.random())
#     for sides in range(i):
#         turtle.right(360/i)
#         turtle.forward(100)

# Challenge 4
# turtle.pensize(10)
# turtle.speed("fastest")
# function_list = [right_forward, left_forward, move_forward, move_backward]
# for n in range(0, 500):
#     turtle.color(random.random(), random.random(), random.random())
#     random.choice(function_list)()

# Challenge 5
turtle.speed("fastest")
for _ in range(0, 72):
    turtle.color(random.random(), random.random(), random.random())
    turtle.circle(100)
    turtle.right(5)

screen.exitonclick()