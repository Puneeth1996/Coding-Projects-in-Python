import turtle
from itertools import cycle


colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])


def draw_circle(size, angle, shift, shape):
    # The background color is now set inside the loop.
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size + 5, angle + 1, shift + 1)



turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)

# can change the below code to 
# turtle.pensize(40)

draw_circle(30, 0, 1)