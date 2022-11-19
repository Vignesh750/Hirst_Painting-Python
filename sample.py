import turtle
import random
govalu = turtle.Turtle()
screen = turtle.Screen()
govalu.speed("slowest")
turtle.colormode(255)
govalu.penup()
govalu.ht()


list_of_colours = [(253, 250, 248), (217, 176, 11), (190, 80, 20), (20, 126, 165), (221, 158, 95),
                   (93, 37, 2), (2, 116, 73), (174, 26, 10), (244, 211, 215), (16, 42, 77), (29, 126, 82),
                   (172, 51, 66), (240, 202, 3), (246, 251, 249), (238, 204, 69), (174, 25, 39), (217, 144, 151),
                   (210, 86, 67), (237, 171, 157), (58, 21, 47), (234, 171, 177), (121, 164, 183), (127, 172, 139),
                   (86, 154, 109), (100, 69, 11), (201, 70, 80), (235, 239, 244), (60, 151, 175), (47, 57, 91),
                   (8, 83, 107)]


def move_turtle_to_start():
    """Moves turtle to the start and returns the position of the turtle"""
    govalu.setheading((180+270)/2)
    govalu.forward(300)
    govalu.setheading(0)
    return govalu.pos()


move_turtle_to_start()


def from_start_draw_dots(colours_list):
    """draws ten dots """
    for i in range(10):
        colour = random.choice(colours_list)
        govalu.dot(20, colour)
        govalu.forward(50)


from_start_draw_dots(list_of_colours)
move_turtle_to_start()






screen.exitonclick()
