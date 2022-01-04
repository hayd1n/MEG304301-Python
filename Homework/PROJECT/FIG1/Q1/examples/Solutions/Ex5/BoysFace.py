from turtle import *
from Face import Face

## Exercise 4: A subclass of Face
## ------------------------------
## The class
##    * Inherits the methods and attributes of its superclass 
##    * Can overide a method
##


class BoysFace (Face) :

    # The class has a constructor. 
    def __init__(self, xpos, ypos, eyeColour):
        super().__init__(xpos, ypos, eyeColour) # Call the Face constructor
        # The next three statement set some attribute suitable this class
        # They can still be changed
        self.setSize(80)         
        self.setNoseSize('large')
        self.setHairLength('short')

    # The draw method needs to be overrriden to includes lashes
    def draw(self):
        super().draw()  # This call the existing draw function
        self.drawBeard()

    # This method can be used to drawlashes. We need to make sure
    # it is called as part of draw.
    def drawBeard(self):
        
        step = 5
        heading = 240
        c = pencolor()
        s = pensize()
        pencolor(self.getHairColour())
        pensize(4)
        while heading <= 300:
            penup()
            setheading(heading)
            forward(int(self.size * 1.1))
            left(90)
            pendown()
            circle(10)
            heading += step
            penup()
            self.goHome()
        pencolor(c)
        pensize(s)
