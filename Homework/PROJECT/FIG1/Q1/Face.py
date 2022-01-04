from turtle import *

# A function is defined for each part, with following steps
#    1. pen up
#    2. move to correct position
#    3. pen down
#    4. draw
#    5. return home

class Face:

    def __init__(self, xpos, ypos):
        self._size = 50
        self._coord = (xpos, ypos)
        self._noseSize = 'normal'

    def setSize(self, radius):
        self._size = radius
        
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
        goto(self._coord)
        setheading(0)
        
    def drawOutline(self):
        penup()
        forward(self._size)
        left(90)
        pendown()
        circle(self._size)
        self.goHome()

    def drawEye(self, turn):
        penup()
        left(turn)
        forward(self._size / 2)
        pendown()
        dot(self._size/10)
        self.goHome()
        
    def drawMouth(self):
        penup()
        right(135)
        forward(self._size/1.7)
        left(90)
        pendown()
        circle(self._size/1.7, 90)
        self.goHome()

    def drawNose(self):
        if self._noseSize == 'large' :
            dot(self._size/2, "grey")
        elif self._noseSize == 'small' :
            dot(self._size/6, "grey")
        else :
            dot(self._size/4, "grey")
        self.goHome()
        

    def drawHairStrand(self, headAngle, headAngleIncrement):
        penup()
        setheading(90)
        forward(self._size)
        pendown()
        segmentLength = int(self._size/6)
        for i in range(5):
            setheading(headAngle)
            headAngle += headAngleIncrement
            forward(segmentLength)
        self.goHome()

    @staticmethod
    def ring(col: str, rad: int):
        """
        Draw a colored circle with a dynamic radius

        Args:
            col (str): Color
            rad (int): Radius
        """
        # Set the fill
        fillcolor(col)
    
        # Start filling the color
        begin_fill()

        # Draw a circle
        circle(rad)
    
        # Ending the filling of the color
        end_fill()