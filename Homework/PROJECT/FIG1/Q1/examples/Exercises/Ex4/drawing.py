from turtle import *
from Face import Face
from GirlsFace import GirlsFace

## Exercise 4
## ----------
## Drawing a specialised Face

# sets the animation speed: can be 'slow'
speed('fast')

# uncomment this to hide the turtle
hideturtle()

# uncomment for instanteneous drawing - no animation
tracer(0)

#  start of drawing code
#  ---------------------

f1 = Face (-200, 0, 'brown')
f1.setSize(80)
f1.setHairColour('black')
f1.setHairLength('short')
f1.setNoseSize('large')
f1.draw()

f2 = GirlsFace (-20, 0, 'blue')
f2.setHairColour('yellow')
f2.draw()


#  ---------------------

# Uncomments to show drawing if no animation
update()

#showturtle()
done()
