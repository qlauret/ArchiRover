from Cardinal import Cardinal
from Planete import PlaneteToroidale
from Point import Point

class Rover:
    def __init__(self,planet: PlaneteToroidale, position_on_planet: Point = Point(1, 1), cardinal: Cardinal = Cardinal()):
        self.point = position_on_planet
        self.planet = planet
        self.cardinal = cardinal

        if position_on_planet.x not in range(1, planet.width + 1):
            print("ERROR: la position X du rover n'est pas sur la planète !")
        if position_on_planet.y not in range(1, planet.height + 1):
            print("ERROR: la position Y du rover n'est pas sur la planète !")
        if self.check_obstacle():
            print("ERROR: le rover est sur un obstacle !")
        self.show_positioning()
    
    def deplacer(self, en_avant: bool):
        previous_position = Point(self.point.x, self.point.y)
        self.cardinal.move_on_cardinal(en_avant, self.point)
        if self.check_obstacle():
            dict_return = {"status": False, "message":{ "type":"obstacle", "message":"Obstacle on way !", "obstacle_position": {"x":self.point.x,"y":self.point.y}}}
            self.point = previous_position
            return dict_return
        else:
            diff = previous_position.less(self.point)
            self.repositionning_on_planet(diff)
        self.show_positioning()
        return {"status": True, "movement": {"x":self.point.x,"y":self.point.y,"o":self.cardinal.direction.value}}
    
    def tourner(self, a_droite: bool):
        self.cardinal.rotate_cardinal(a_droite)
        self.show_positioning()
        return {"status": True, "movement": {"x":self.point.x,"y":self.point.y,"o":self.cardinal.direction.value}}

    def repositionning_on_planet(self, diff):
        if self.point.x not in range(1, self.planet.width + 1):
            # print("ERROR: la position X du rover n'est pas sur la planète !")
            print("Le rover à fait le tour de la planète en x !!")
            if diff.x > 0:
                self.point.x = self.planet.width
            else:
                self.point.x = 1
        if self.point.y not in range(1, self.planet.height + 1):
            # print("ERROR: la position Y du rover n'est pas sur la planète !")
            print("Le rover à fait le tour de la planète en y !!")
            if diff.y > 0:
                self.point.y = self.planet.height
            else:
                self.point.y = 1
        
    def check_obstacle(self):
        for obstacle in self.planet.obstacle_on_planet:
            if obstacle.point.isEqual(self.point):
                print("** IL y a un obstacle sur votre chemin **")
                return True
        return False
        
    def show_positioning(self):
        print("({}, {}) -> {}".format(self.point.x, self.point.y, self.cardinal.direction.value))

