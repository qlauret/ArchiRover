from MissionControl import *

class Cartographie:
    def __init__(self):
        self.tailleX = 10
        self.tailleY = 10
        self.roverLastPosition = Point(3, 4)
        self.roverLastOrientation = "Est"
        self.listObstacles = []
        self.listPointsVisited = []

    def displayCarto(self):
        print(" _______________________ ")
        print("|O   O          O       |")
        print("|O        O     O       |")
        print("|    O                 O|")
        print("|       V       O       |")
        print("|     O        O        |")
        print("|                       |")
        print("|        O         O    |")
        print(" ----------------------- ")

    def processResponse(self, responseString):
        print(f"response: {responseString}")
        subStrings = responseString.split("|")
        for subString in subStrings:
            elements = subString.split(",")
            if 3 <= len(elements) <= 4:
                pos_x = elements[0]
                pos_y = elements[1]
                orientation = elements[2]
                isObstacle = False
                if len(elements) == 4:
                    if elements[3] == "X":
                        isObstacle = True
                # ENREGISTRER LA POSITION ET L'OBSCTACLE
                int_x, int_y = int(pos_x), int(pos_y)
                if isObstacle:
                    print(f"AJOUT OBSTACLE SUR {pos_x},{pos_y}")
                    self.listObstacles.append((int_x, int_y))
                else:
                    print(f"SAVE PASSAGE rover: {pos_x},{pos_y} ->{orientation}")
                    self.roverLastPosition = (int_x, int_y)
                    self.roverLastOrientation = orientation
                    self.listPointsVisited.append(self.roverLastPosition)
            else:
                print("NON RECONNU")

    def stringOrientationToCardinal(self, orientation):
        if orientation == "North":
            return "Nord"
        elif orientation == "East":
            return "Est"
        elif orientation == "West":
            return "Ouest"
        elif orientation == "South":
            return "South"
        else:
            return "Nord"

    def cardinalToString(self, cardinal):
        if cardinal == "Nord":
            return "^"
        elif cardinal == "Est":
            return ">"
        elif cardinal == "South":
            return "V"
        elif cardinal == "Ouest":
            return "<"
