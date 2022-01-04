from turtle import *
from Face import Face

## Exercise 1
## ----------
## Simple drawing

# sets the animation speed: can be 'slow'
speed('fast')

# uncomment this to hide the turtle
# hideturtle()

# uncomment for instanteneous drawing - no animation
tracer(0)

#  start of drawing code
#  ---------------------

xStart = -250
startSize = 90
sizeDecrement = 15

xPos = xStart
size = startSize
while size > 10:
    f = Face (xPos, 0)
    f.setSize(size)
    f.draw()
    xPos = xPos + 2*size + 10
    size = size - sizeDecrement
#  ---------------------

# Uncomments to show drawing if no animation
# update()

showturtle()
done()
