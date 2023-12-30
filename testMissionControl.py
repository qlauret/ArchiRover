import unittest
from unittest.mock import patch
from io import StringIO
from Cartographie import Cartographie
from MissionControl import MissionControl

class TestMissionControl(unittest.TestCase):
    def setUp(self):
        self.carto = Cartographie()
        self.mc = MissionControl(self.carto)

    def test_firstInterface_choixA(self):
        with patch('builtins.input', side_effect=['A']):
            result = self.mc.firstInterface()
            self.assertEqual(result, 'A')

    def test_firstInterface_choixB(self):
        with patch('builtins.input', side_effect=['B']):
            result = self.mc.firstInterface()
            self.assertEqual(result, 'B')

    def test_firstInterface_quitter(self):
        with patch('builtins.input', side_effect=['E']):
            result = self.mc.firstInterface()
            self.assertEqual(result, 'E')

    def test_roverInterface_avancer(self):
        with patch('builtins.input', side_effect=['Z']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.mc.roverInterface()
                output = fake_output.getvalue().strip()
                self.assertEqual(output, "ENVOI DES INSTRUCTIONS AU ROVER")

    def test_roverInterface_reculer(self):
        with patch('builtins.input', side_effect=['S']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.mc.roverInterface()
                output = fake_output.getvalue().strip()
                self.assertEqual(output, "ENVOI DES INSTRUCTIONS AU ROVER")

    def test_roverInterface_rotationGauche(self):
        with patch('builtins.input', side_effect=['Q']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.mc.roverInterface()
                output = fake_output.getvalue().strip()
                self.assertEqual(output, "ENVOI DES INSTRUCTIONS AU ROVER")

    def test_roverInterface_rotationDroite(self):
        with patch('builtins.input', side_effect=['D']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.mc.roverInterface()
                output = fake_output.getvalue().strip()
                self.assertEqual(output, "ENVOI DES INSTRUCTIONS AU ROVER")

    def test_roverInterface_quitter(self):
        with patch('builtins.input', side_effect=['E']):
            self.mc.exitProgramm = unittest.mock.Mock()
            self.mc.roverInterface()
            self.mc.exitProgramm.assert_called_once_with("ANNULER")

    def test_roverInterface_commandeInconnue(self):
        with patch('builtins.input', side_effect=['X']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                self.mc.roverInterface()
                output = fake_output.getvalue().strip()
                self.assertEqual(output, "-- Désolé, la commande X n'est pas reconnue. --")

    def test_exitProgramm(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.mc.exitProgramm("TERMINE !")
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "TERMINE !")

if __name__ == '__main__':
    unittest.main()