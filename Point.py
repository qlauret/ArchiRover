class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, p):
        new_x = self.x + p.x
        new_y = self.y + p.y
        return Point(new_x, new_y)
    def less(self, p):
        new_x = self.x - p.x
        new_y = self.y - p.y
        return Point(new_x, new_y)
    
    def isEqual(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    def to_dict(self):
        return {"x": self.x, "y": self.y}
    