import turtle as t
from random import randint, random


def draw_star(ranPts, size, col, x, y):
    t.penup()
    t.goto(ranX, ranY)
    t.pendown()
    angle = 180 - (180 / ranPts)
    t.color(ranCol)
    t.begin_fill()
    for i in range(ranPts):
        t.forward(ranSize)
        t.right(angle)
    t.end_fill()

while True:
    ranPts = randint(2, 5) * 2 + 1
    ranSize = randint(10, 50)
    ranCol = (random(), random(), random())
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)
    # Main code
    t.Screen().bgcolor('dark blue')
    draw_star(ranPts, ranSize, ranCol, ranX, ranY)
    t.hideturtle()