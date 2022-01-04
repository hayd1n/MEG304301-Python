from turtle import *

## Exercise 3 Hair Class
## --------------------
## The Hair knows which face it is part of so it can get 
##  the position of the face

class Hair:

    def __init__(self, face):
        self.myFace = face
        self.length = 'short'
        self.colour = 'black'

    # Length is short, sholder or long
    def setLength(self, length):
        self.length = length

    # Colour is one understand by Python
    def setColour(self, c):
        self.colour = c


    def draw(self):
        c = pencolor()
        pencolor(self.colour)
        pensize(5)
        self.drawHairStrand(-15, -17)
        self.drawHairStrand(0, -17)
        self.drawHairStrand(15, -17)
        self.drawHairStrand(165, 17)
        self.drawHairStrand(180, 17)
        self.drawHairStrand(195, 17)
        pencolor(c)


# --------------------------------------------------
#    Functions that are called from with the class
# --------------------------------------------------

    def drawHairStrand(self, headAngle, headAngleIncrement):
        penup()
        setheading(90)
        forward(self.myFace.size)
        segmentLength = int(self.myFace.size/6)
        strands = 0 # no hair
        if self.length == 'short':
            segs = 4
        elif self.length == 'shoulder':
            segs = 8
        elif self.length == 'long':
            segs = 16
            
        pendown()
        setheading(headAngle)
        for i in range(segs):
            forward(segmentLength)
            if heading() < 240 or heading() > 300:
                headAngle += headAngleIncrement
                setheading(headAngle)
        self.myFace.goHome()
