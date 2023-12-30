from Point import Point
from Cardinal import Cardinal

class Cartographie:
    def __init__(self):
        self.tailleX = 10
        self.tailleY = 10
        self.roverLastPosition = Point(0, 0)
        self.roverLastOrientation = Cardinal.direction.North
        self.listObstacles = []
        self.listPointsVisited = []

    
    def processResponse(self, responseJson):
        status = responseJson["status"]
        log_movement = responseJson["log_movement"]
        
        # On met à jour la liste des points visités
        for point in log_movement:
            new_point = Point(point["x"], point["y"])
            if not self.is_point_visited(new_point):
                self.listPointsVisited.append(new_point)
        if status:
            # On met à jour la position et l'orientation du rover
            last_position = responseJson["log_movement"][-1]
            self.roverLastPosition = Point(last_position["x"], last_position["y"])
            self.roverLastOrientation = Cardinal.direction.fromValue(last_position["o"])

        else:
            # Si le déplacement a échoué, on enregistre l'obstacle
            error = responseJson["error"]
            if error["type"] == "obstacle":
                obstacle_position = Point(error["obstacle_position"]["x"], error["obstacle_position"]["y"])
                if not self.is_obstacle(obstacle_position):
                    self.listObstacles.append(obstacle_position)

    def is_point_visited(self, point):
        for visited_point in self.listPointsVisited:
            if visited_point.isEqual(point):
                return True
        return False

    def is_obstacle(self, obstacle):
        for obstacle_point in self.listObstacles:
            if obstacle_point.isEqual(obstacle):
                return True
        return False
                
                
    def displayCarto(self):
        print(" *** CARTOGRAPHIE *** ")
        print("visited: %s" % [point.to_dict() for point in self.listPointsVisited])
        print("obstacles: %s" % [obstacle.to_dict() for obstacle in self.listObstacles])
        print("rover: %s %s" % (self.cardinalToString(self.roverLastOrientation.value), self.roverLastPosition.to_dict()))


    def cardinalToString(self, cardinal):
        if cardinal == "N":
            return "^"
        elif cardinal == "E":
            return ">"
        elif cardinal == "S":
            return "V"
        elif cardinal == "W":
            return "<"
