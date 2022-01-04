from turtle import *

## Exercise 3 Eye Class
## --------------------
## The Eye knows which face it is part of so it can get 
##  the position of the face



class Eye:

    def __init__(self, face, side, colour):
        self.myFace = face
        self.side = side
        self.colour = colour        

    def draw(self):
        penup()
        if self.side == 'left':
            setheading(135)
            rotation = 90
        else:
            setheading(45)
            rotation = 180
        forward(self.myFace.getSize() / 2)
        pendown()
        dot(self.myFace.getSize() / 10, self.colour)

        penup()
        left(rotation)
        forward(self.myFace.getSize() / 6)
        pendown()
        left(90)
        circle(self.myFace.getSize() / 6, 90)
        self.myFace.goHome()

# --------------------------------------------------
#    Functions that are called from with the class
# --------------------------------------------------

