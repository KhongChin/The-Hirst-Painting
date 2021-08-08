import colorgram
import random
import turtle as t

colors = colorgram.extract("Hirst_Painting.jpg", 35)
list_of_colors = []

for n in range(35):
    list_of_rgb = [colors[n].rgb.r, colors[n].rgb.g, colors[n].rgb.b]
    tuple_of_rgb = tuple(list_of_rgb)
    list_of_colors.append(tuple_of_rgb)

color_list = list_of_colors[3:]  # First 3 colors are white

turtle = t.Turtle()
screen = t.Screen()
t.colormode(255)

turtle.hideturtle()
turtle.penup()
x = -250.00
y = -250.00
turtle.goto(x, y)
turtle.speed("fastest")

for _ in range(10):
    for _ in range(10):
        turtle.color(random.choice(color_list))
        turtle.forward(50)
        turtle.dot(size=20)
    y += 50
    turtle.goto(x, y)


screen.exitonclick()
