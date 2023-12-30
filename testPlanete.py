import unittest
from Obstacle import Obstacle
from Point import Point
from Planete import PlaneteToroidale

class TestPlaneteToroidale(unittest.TestCase):
    def setUp(self):
        self.planet = PlaneteToroidale()

    def test_add_obstacle_inside_planet(self):
        obstacle = Obstacle(Point(5, 5))
        self.planet.add_obstacle(obstacle)
        self.assertIn(obstacle, self.planet.obstacle_on_planet)

    def test_add_obstacle_outside_planet(self):
        obstacle = Obstacle(Point(15, 5))
        self.planet.add_obstacle(obstacle)
        self.assertNotIn(obstacle, self.planet.obstacle_on_planet)

if __name__ == '__main__':
    unittest.main()