import unittest
from unittest.mock import patch
from io import StringIO
from mainTopologie import initPlanet

class TestInitPlanet(unittest.TestCase):
    @patch('builtins.input', side_effect=['5', '4', '3'])
    def test_initPlanet_validInput(self, mock_input):
        expected_width = 5
        expected_height = 4
        expected_nb_obstacle = 3

        result = initPlanet()

        self.assertEqual(result.width, expected_width)
        self.assertEqual(result.height, expected_height)
        self.assertEqual(len(result.obstacle_on_planet), expected_nb_obstacle)

    @patch('builtins.input', side_effect=['2', '4', '3', '5', '3'])
    def test_initPlanet_invalidWidth(self, mock_input):
        expected_error = "La largeur de la planète doit être supérieure à 3."

        with patch('sys.stdout', new=StringIO()) as fake_out:
            initPlanet()

        self.assertIn(expected_error, fake_out.getvalue())

    @patch('builtins.input', side_effect=['5', '2', '3', '5', '3'])
    def test_initPlanet_invalidHeight(self, mock_input):
        expected_error = "La hauteur de la planète doit être supérieure à 3."

        with patch('sys.stdout', new=StringIO()) as fake_out:
            initPlanet()

        self.assertIn(expected_error, fake_out.getvalue())

    @patch('builtins.input', side_effect=['5', '4', '26', '5', '3'])
    def test_initPlanet_invalidNbObstacle(self, mock_input):
        expected_error = "Le nombre d'obstacles ne peut pas dépasser 19."

        with patch('sys.stdout', new=StringIO()) as fake_out:
            initPlanet()

        self.assertIn(expected_error, fake_out.getvalue())

if __name__ == '__main__':
    unittest.main()