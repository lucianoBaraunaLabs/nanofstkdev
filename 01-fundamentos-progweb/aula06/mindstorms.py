# -*- coding: utf-8 -*-

import turtle

def draw_square(some_thurtle):
    for i in range(1,5):
        some_thurtle.forward(100)
        some_thurtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(100)
    draw_square(brad)
    for i in range(1, 37):
        draw_square(brad)
        brad.right(10)
    #Create the turtle Angie - Draws a circle
    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)

    window.exitonclick()

draw_art()