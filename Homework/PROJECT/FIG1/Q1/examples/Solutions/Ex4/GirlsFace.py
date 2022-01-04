from turtle import *
from Face import Face

## Exercise 4: A subclass of Face
## ------------------------------
## The class
##    * Inherits the methods and attributes of its superclass 
##    * Can overide a method
##


class GirlsFace (Face) :

    # The class has a constructor. 
    def __init__(self, xpos, ypos, eyeColour):
        super().__init__(xpos, ypos, eyeColour) # Call the Face constructor
        # The next three statement set some attribute suitable this class
        # They can still be changed
        self.setSize(70)         
        self.setNoseSize('normal')
        self.setHairLength('shoulder')

    # The draw method needs to be overrriden to includes lashes
    def draw(self):
        super().draw()  # This call the existing draw function
        self.drawLashes() 

    # This methid can be used to drawlashes. We need to make sure
    # it is called as part of draw.
    def drawLashes(self):
        lashes = [[140, 120, 100, 80, 60], [50, 70, 90, 110, 130]]
        eyeAngles = [135, 45]
        c = pencolor()
        pencolor(self.getHairColour())
        for i in range(len(lashes)):
            setheading(eyeAngles[i])
            forward(int(self.size/2) )
            for j in range(len(lashes[i])):
                setheading(lashes[i][j])
                forward(5)
                pensize(2)
                pendown()
                forward(5)
                penup()
                backward(10)            
            self.goHome()
        pencolor(c)
