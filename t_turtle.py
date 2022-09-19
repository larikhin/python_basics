import turtle
#from tkinter import *

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    t.pensize(1)
    collist = ['red','blue','white','green']
    for i in range(4):
        t.pencolor(collist[i])
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()      # Set up the window and its attributes
wn.bgcolor("black")


alex = turtle.Turtle()    # create alex

for i in range(20):
    drawSquare(alex, 50+i)      # Call the function to draw the square passing the actual turtle and the actual side size
wn.exitonclick()


