
## Exercise 5
## ----------
## Family Portrait

class Family:

    def __init__(self):
        self.faces = []

    def add(self, f):
        self.faces.append(f)

    def draw(self):
        for f in self.faces:
            f.draw()
            
