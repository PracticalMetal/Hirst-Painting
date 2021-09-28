from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

hirst_painting=Turtle()
# setting the turtle to be invisible so as to get a clean output
hirst_painting.hideturtle()
# hirst_painting.penup()
# hirst_painting.setpos(-100,-100)
# hirst_painting.pendown()

# random colour extracted from the hirst painting
colour_list=[(201, 164, 112), (238, 246, 241), (152, 75, 49), (221, 201, 138), (171, 153, 42), (56, 95, 126), (139, 31, 19), (134, 163, 184), (197, 93, 73), (48, 121, 88), (98, 75, 77), (142, 178, 148), (75, 41, 33), (165, 145, 156), (15, 99, 71), (234, 175, 164), (54, 45, 47), (32, 61, 77), (145, 21, 25), (21, 83, 89), (182, 205, 175), (85, 147, 127), (44, 66, 87), (178, 94, 98), (222, 177, 184), (8, 68, 51), (108, 127, 151)]

# setting two for loop and using setpos method to move the turtle
for i in range(10):
    for j in range(10):
        hirst_painting.color(random.choice(colour_list))
        hirst_painting.penup()
        hirst_painting.setpos((j+1)*100-500,(i+1)*100-480)
        hirst_painting.pendown()
        hirst_painting.dot(20)

screen=Screen()
screen.exitonclick()