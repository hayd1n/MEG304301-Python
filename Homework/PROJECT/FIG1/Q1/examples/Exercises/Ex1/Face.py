from turtle import *

## Exercise 1 [Do not change this in Ex 1]
## ----------
## Simple face class
## Position is centre of face
##     Size is radius

# A function is defined for each part, with following steps
#    1. pen up
#    2. move to correct position
#    3. pen down
#    4. draw
#    5. return home

class Face:

    def __init__(self, xpos, ypos):
        self.size = 50
        self.coord = (xpos, ypos)
        self.noseSize = 'normal'

    def setSize(self, radius):
        self.size = radius
        
    def draw(self):
        self.goHome()
        pensize(2)
        self.drawOutline()
        self.drawEye(135)
        self.drawEye(45)
        self.drawMouth()
        self.drawNose()
        pensize(5)
        self.drawHairStrand(-15, -17)
        self.drawHairStrand(0, -17)
        self.drawHairStrand(15, -17)
        self.drawHairStrand(165, 17)
        self.drawHairStrand(180, 17)
        self.drawHairStrand(195, 17)

# --------------------------------------------------
#    Functions that are called from with the class
# --------------------------------------------------


    # After drawing each part, turtle position 
    # returns to centre. Parts can be drawn in any order
    def goHome(self):
        penup()
        goto(self.coord)
        setheading(0)
        
    def drawOutline(self):
        penup()
        forward(self.size)
        left(90)
        pendown()
        circle(self.size)
        self.goHome()

    def drawEye(self, turn):
        penup()
        left(turn)
        forward(self.size / 2)
        pendown()
        dot(self.size/10)
        self.goHome()
        
    def drawMouth(self):
        penup()
        right(135)
        forward(self.size/1.7)
        left(90)
        pendown()
        circle(self.size/1.7, 90)
        self.goHome()

    def drawNose(self):
        if self.noseSize == 'large' :
            dot(self.size/2, "grey")
        elif self.noseSize == 'small' :
            dot(self.size/6, "grey")
        else :
            dot(self.size/4, "grey")
        self.goHome()
        

    def drawHairStrand(self, headAngle, headAngleIncrement):
        penup()
        setheading(90)
        forward(self.size)
        pendown()
        segmentLength = int(self.size/6)
        for i in range(5):
            setheading(headAngle)
            headAngle += headAngleIncrement
            forward(segmentLength)
        self.goHome()
 

