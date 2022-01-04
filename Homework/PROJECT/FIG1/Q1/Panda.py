from turtle import *
from Face import Face

class Panda(Face):

    def __init__(self, xpos, ypos):
        super().__init__(xpos, ypos)

    def draw(self):
        self.goHome()
        pensize(4)
        self.drawEars()
        self.drawOutline()
        self.drawEyes()
        self.drawNose()
        self.drawMouth()

    def drawEars(self):
        radius = self._size * 0.3636

        # Draw first ear
        left(45)
        forward(self._size - radius * 0.5)
        right(90)
        pendown()
        Face.ring('black', radius)
        penup()
        self.goHome()
        
        # Draw second ear
        left(45 + 90)
        forward(self._size - radius * 0.5)
        right(90)
        pendown()
        Face.ring('black', radius)
        penup()
        self.goHome()

    def drawOutline(self):
        forward(self._size)
        left(90)
        pendown()
        Face.ring('white', self._size)
        penup()
        self.goHome()

    def drawEyes(self):
        ##### Draw eyes black #####
        
        # Draw first eye
        penup()
        left(45)
        forward(self._size * 0.3)
        right(90)
        pendown()
        Face.ring('black', self._size * 0.1818)
        self.goHome()
        
        # Draw second eye
        penup()
        left(45 + 90)
        forward(self._size * 0.3)
        right(90)
        pendown()
        Face.ring('black', self._size * 0.1818)
        self.goHome()
        
        ##### Draw eyes white #####
        
        # Draw first eye
        penup()
        left(45)
        forward(self._size * 0.32)
        right(90)
        pendown()
        Face.ring('white', self._size * 0.0909)
        self.goHome()
        
        # Draw second eye
        penup()
        left(45 + 90)
        forward(self._size * 0.32)
        right(90)
        pendown()
        Face.ring('white', self._size * 0.0909)
        self.goHome()

    def drawNose(self):
        penup()
        right(90)
        forward(self._size * 0.2)
        right(90)
        pendown()
        Face.ring('black', self._size * 0.1272)
        self.goHome()

    def drawMouth(self):
        penup()
        right(90)
        forward(self._size * 0.2 + (self._size * 0.1272) * 2)
        pendown()
        circle(self._size * 0.1818, 180)
        penup()
        self.goHome()
        right(90)
        forward(self._size * 0.2 + (self._size * 0.1272) * 2)
        pendown()
        left(180)
        circle(self._size * 0.1818, -180)
        self.goHome()