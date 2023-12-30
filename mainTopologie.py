from Obstacle import Obstacle
from Planete import PlaneteToroidale
from Point import Point
import random

def initPlanet():
    print("** INITIALISATION PLANETE **")
    #LARGEUR
    while True:
        try:
            widthPlanet = int(input("Entrez la largeur de la planète : "))
            if widthPlanet < 3:
                print("La largeur de la planète doit être supérieure à 3.")
            else:
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    #HAUTEUR
    while True:
        try:
            heightPlanet = int(input("Entrez la hauteur de la planète : "))
            if heightPlanet < 3:
                print("La hauteur de la planète doit être supérieure à 3.")
            else:
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    #NB OBSTACLES
    while True:
        try:
            nb_obstacle = int(input("Entrez le nombre d'obstacles à ajouter : "))
            if nb_obstacle > (widthPlanet * heightPlanet) - 1:
                print("Le nombre d'obstacles ne peut pas dépasser %s." % ((widthPlanet * heightPlanet) - 1))
            else:
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    Mars = PlaneteToroidale(width=widthPlanet, height=heightPlanet)
    obstacle_coordinates = []

    for _ in range(nb_obstacle):
        while True:
            x = random.randint(1, Mars.width)
            y = random.randint(1, Mars.height)
            if (x, y) not in obstacle_coordinates:
                obstacle_coordinates.append((x, y))
                obstacle = Obstacle(Point(x, y))
                Mars.add_obstacle(obstacle)
                break

    return Mars