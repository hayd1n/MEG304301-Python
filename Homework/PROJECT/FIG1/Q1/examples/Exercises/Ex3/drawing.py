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

f1 = Face (-200, 0)
f1.setSize(80)
f1.setHairColour('black')
f1.setHairLength('short')
f1.setNoseSize('large')
f1.draw()

f2 = Face (-20, 0)
f2.setSize(80)
f2.setHairColour('brown')
f2.setHairLength('shoulder')
f2.setNoseSize('normal')
f2.draw()

f3 = Face (160, 0)
f3.setSize(80)
f3.setHairColour('pink')
f3.setHairLength('long')
f3.setNoseSize('small')
f3.draw()

#  ---------------------

# Uncomments to show drawing if no animation
# update()

showturtle()
done()
