class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, p):
        newX = self.x + p.x
        newY = self.y + p.y
        return Point(newX, newY)
