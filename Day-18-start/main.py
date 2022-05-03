import turtle as t
import random

def polygon(side):
    for i in range(side):
        tim.right(360/side)
        tim.forward(100)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim = t.Turtle()
t.colormode(255)

directions = [0, 90, 180, 270]

# tim.pensize(15)
tim.speed("fastest")

def spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


spirograph(10)





# RANDOM WALK
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# CREATING A POLYGON USING TURTLE
# side = 3
# color_index = 0
#
# should_continue = True
# while should_continue:
#     color = color_list[color_index]
#     tim.color(color)
#     polygon(side)
#     side += 1
#     color_index += 1
#     if side == 10:
#         should_continue = False
#
screen = t.Screen()
screen.exitonclick()


