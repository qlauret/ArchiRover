from Point import Point

class Obstacle:
    point : Point
    def __init__(self, point: Point):
        self.point = point
    def to_dict(self):
        return {"x": self.x, "y": self.y}