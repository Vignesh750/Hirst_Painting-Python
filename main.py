# import colorgram
import random
import turtle as t

t.colormode(255)

govalu = t.Turtle()
govalu.speed("fastest")
govalu.ht()
screen = t.Screen()
screen.bgcolor("black")
govalu.penup()
govalu.backward(250)
govalu.right(90)
govalu.forward(250)
position = govalu.pos()
govalu.left(90)

list_of_colours = [(253, 250, 248), (217, 176, 11), (190, 80, 20), (20, 126, 165), (221, 158, 95), (93, 37, 2),
                   (2, 116, 73), (174, 26, 10), (244, 211, 215), (16, 42, 77), (29, 126, 82), (172, 51, 66),
                   (240, 202, 3), (246, 251, 249), (238, 204, 69), (174, 25, 39), (217, 144, 151), (210, 86, 67),
                   (237, 171, 157), (58, 21, 47), (234, 171, 177), (121, 164, 183), (127, 172, 139), (86, 154, 109),
                   (100, 69, 11), (201, 70, 80), (235, 239, 244), (60, 151, 175), (47, 57, 91), (8, 83, 107)]
for m in range(10):
    for i in range(10):
        colour = random.choice(list_of_colours)
        govalu.dot(20, colour)
        govalu.forward(distance=50)
    govalu.goto(position)
    govalu.left(90)
    govalu.forward(50)
    govalu.right(90)
    position = govalu.pos()

screen.exitonclick()
# e.g. (255, 151, 210)
