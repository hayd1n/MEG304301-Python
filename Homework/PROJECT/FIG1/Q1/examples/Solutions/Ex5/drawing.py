from turtle import *
from GirlsFace import GirlsFace
from BoysFace import BoysFace
from ChildsFace import ChildsFace
from Family import Family
import random

## Exercise 5
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

fam = Family()

b = BoysFace (-100, 200, 'brown')
b.setHairColour('black')
fam.add(b)
g = GirlsFace (80, 200, 'blue')
g.setHairColour('brown')
fam.add(g)
num = random.choice([2,3,4,5])
xpos = [0, 150, -150, 300, -300]
for n in range(num):
    fam.add(ChildsFace(xpos[n], 0))
            
fam.draw()

#  ---------------------

# Uncomments to show drawing if no animation
#update()

#showturtle()
done()
