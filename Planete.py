from Obstacle import Obstacle
from Point import Point


class PlaneteToroidale:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.obstacle_on_planet = []

    def add_obstacle(self, obstacle: Obstacle):
        if not (1 <= obstacle.point.x <= self.width):
            print("ERROR: la position X de l'obstacle n'est pas sur la planète !")
        else:
            if not (1 <= obstacle.point.y <= self.height):
                print("ERROR: la position Y de l'obstacle n'est pas sur la planète !")
            else:
                # tout est ok, l'obstacle est bien sur la planète
                self.obstacle_on_planet.append(obstacle)
