from turtle import *
from Panda import Panda

# sets the animation speed: can be 'slow'
speed('slow')

# uncomment for instanteneous drawing - no animation
# tracer(0)

p = Panda(0, 0)
p.setSize(110)
p.draw()

# Uncomments to show drawing if no animation
# update()

hideturtle()
done()