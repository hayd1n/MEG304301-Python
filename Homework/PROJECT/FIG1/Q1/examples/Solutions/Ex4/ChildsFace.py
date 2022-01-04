from turtle import *
from Face import Face
import random

## Exercise 4: A subclass of Face
## ------------------------------
## The class
##    * Inherits the methods and attributes of its superclass 
##    * Can overide a method
##


class ChildsFace (Face) :

    # The class has a constructor. 
    def __init__(self, xpos, ypos):
        
        super().__init__(xpos, ypos, random.choice(['blue', 'brown'])) # Call the Face constructor
        # The next three statement set some attribute suitable this class
        # They can still be changed
        self.setSize(random.choice([40, 50, 60]))         
        self.setNoseSize('small')
        hlen = random.choice(['short', 'long'])
        self.setHairLength(hlen)
        if hlen == 'short':
            self.setHairColour(random.choice(['black', 'brown']))
        else:
            if self.getSize() == 60:
                self.setHairColour(random.choice(['yellow', 'pink', 'green']))
            else:    
                self.setHairColour(random.choice(['yellow', 'brown', 'black']))


    # The draw method needs to be overrriden to spots
    def draw(self):
        super().draw()  # This call the existing draw function
        if self.getSize() in [50, 60]:
            if random.random() > 0.3:
                self.drawSpots() 

    # This method can be used to draw spots. We need to make sure
    # it is called as part of draw.
    def drawSpots(self):
        angles = [225, 315]
        for a in angles:
            setheading(a)
            forward(int(self.size/3) )
            for j in range(5):
                m = random.randrange(5, 8)
                d = random.randrange(0, 360)
                setheading(d)
                forward(m)
                pendown()
                dot(3, 'red')
                penup()
                backward(m)            
            self.goHome()

