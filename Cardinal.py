from enum import Enum

class CardinalDirection(Enum):
    North = "N"
    East = "E"
    South = "S"
    West = "W"
    @classmethod
    def fromValue(cls, value):
        for direction in cls:
            if direction.value == value:
                return direction
        raise ValueError(f"Invalid value: {value}")
    
class Cardinal:
    direction = CardinalDirection.North
    # def __init__(self, cardinal:CardinalDirection = CardinalDirection.West):
    #     self.direction = cardinal

    def move_on_cardinal(self, go_forward, point):
        if self.direction == CardinalDirection.North:
            if go_forward:
                point.y += 1
            else:
                point.y -= 1
        elif self.direction == CardinalDirection.East:
            if go_forward:
                point.x += 1
            else:
                point.x -= 1
        elif self.direction == CardinalDirection.South:
            if go_forward:
                point.y -= 1
            else:
                point.y += 1
        elif self.direction == CardinalDirection.West:
            if go_forward:
                point.x -= 1
            else:
                point.x += 1
        
    def rotate_cardinal(self, on_right):
        if on_right:
            if self.direction == CardinalDirection.North:
                self.direction = CardinalDirection.East
            elif self.direction == CardinalDirection.East:
                self.direction = CardinalDirection.South
            elif self.direction == CardinalDirection.South:
                self.direction = CardinalDirection.West
            elif self.direction == CardinalDirection.West:
                self.direction = CardinalDirection.North
        else:
            if self.direction == CardinalDirection.North:
                self.direction = CardinalDirection.West
            elif self.direction == CardinalDirection.East:
                self.direction = CardinalDirection.North
            elif self.direction == CardinalDirection.South:
                self.direction = CardinalDirection.East
            elif self.direction == CardinalDirection.West:
                self.direction = CardinalDirection.South