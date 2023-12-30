from contextlib import redirect_stdout
import io
import unittest
from Obstacle import Obstacle
from Rover import Rover
from Planete import PlaneteToroidale
from Point import Point
from Cardinal import Cardinal

class TestRover(unittest.TestCase):
    def setUp(self):
        self.Mars = PlaneteToroidale(5, 5)
        self.rover = Rover(self.Mars, Point(2, 2))

    def test_deplacer(self):
        result = self.rover.deplacer(en_avant=True)
        self.assertTrue(result["status"])
        self.assertEqual(result["movement"]["x"], 2)
        self.assertEqual(result["movement"]["y"], 3)

    def test_tourner(self):
        result = self.rover.tourner(a_droite=True)
        self.assertTrue(result["status"])
        self.assertEqual(result["movement"]["o"], "E")

    def test_repositionning_on_planet(self):
        diff = Point(3, 0)
        self.rover.repositionning_on_planet(diff)
        self.assertEqual(self.rover.point.x, 1)
        self.assertEqual(self.rover.point.y, 2)

    def test_check_obstacle(self):
        obstacle = Obstacle(Point(2, 3))
        self.Mars.obstacle_on_planet.append(obstacle)
        result = self.rover.check_obstacle()
        self.assertTrue(result)

    def test_show_positioning(self):
        expected_output = "(2, 2) -> N"
        with io.StringIO() as buf, redirect_stdout(buf):
            self.rover.show_positioning()
            output = buf.getvalue().strip()
            self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()