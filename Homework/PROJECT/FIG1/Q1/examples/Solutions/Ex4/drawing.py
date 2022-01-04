from turtle import *
from GirlsFace import GirlsFace
from BoysFace import BoysFace
from ChildsFace import ChildsFace

## Exercise 4
## ----------
## Drawing a specialised Face

# sets the animation speed: can be 'slow'
speed('fast')

# uncomment this to hide the turtle
#hideturtle()

# uncomment for instanteneous drawing - no animation
tracer(0)

#  start of drawing code
#  ---------------------

f1 = BoysFace (-100, 100, 'brown')
f1.setHairColour('black')
f1.draw()

f2 = GirlsFace (80, 100, 'blue')
f2.setHairColour('yellow')
f2.draw()

f3 = ChildsFace(220, 100)
f3.draw()

#  ---------------------

# Uncomments to show drawing if no animation
#update()

#showturtle()
done()
