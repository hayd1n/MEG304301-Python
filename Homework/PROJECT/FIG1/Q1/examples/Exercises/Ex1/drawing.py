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
# tracer(0)

#  start of drawing code
#  ---------------------
  
f1 = Face(0, 0)
f1.draw()
        
f2 = Face(-200, 0)
f2.setSize(80)
f2.draw()

#  ---------------------

# Uncomments to show drawing if no animation
# update()

showturtle()
done()
