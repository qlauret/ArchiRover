import time
from Cardinal import Cardinal
from Point import Point
from Rover import Rover
from SocketAdapter import SocketAdapter
from mainTopologie import *

def main():
    print("MAIN ROVER LAUNCHED")
    Mars = initPlanet()
    #POSITION X
    while True:
        try:
            posX = int(input("Entrez la position X du Rover : "))
            if posX not in range(1,Mars.width):
                print("La position X du Rover doit être comprise entre 1 et %s." % Mars.width)
            else:
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    #POSITION Y
    while True:
        try:
            posY = int(input("Entrez la position Y du Rover : "))
            if posY not in range(1,Mars.height):
                print("La position Y du Rover doit être comprise entre 1 et %s." % Mars.height)
            else:
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            
    Curiosity = Rover(Mars, Point(posX, posY))
    print("INIT ROVER OK")
    
    while True:
        receiver = SocketAdapter()
        received_data = receiver.dataReceiver()
        print("Données reçues:", received_data)
        
        
        if received_data.get('command'):
            feedback = {
                "status": True,
                "log_movement": [{"x":Curiosity.point.x,"y":Curiosity.point.y,"o":Curiosity.cardinal.direction.value}],
                "error": {}
            }
            for char in received_data.get('command'):
                #Interpréter les commandes reçues
                if char == "Z":
                    infosBack = Curiosity.deplacer(en_avant=True)
                elif char == "S":
                    infosBack = Curiosity.deplacer(en_avant=False)
                elif char == "D":
                    infosBack = Curiosity.tourner(a_droite=True)
                elif char == "Q":
                    infosBack = Curiosity.tourner(a_droite=False)
                    
                #Ajouter les infos de retour du Rover dans le feedback
                if infosBack and "status" in infosBack and infosBack["status"]:
                    #Status infosBack est True
                    feedback["log_movement"].append(infosBack.get("movement"))
                elif infosBack and "status" in infosBack and not infosBack["status"]:
                    #Status infosBack est False
                    feedback["status"] = False
                    feedback["error"] = infosBack.get("message")
                    break
                else:
                    feedback["status"] = False
                    feedback["error"] = {"type":"unknown", "message":"Unknown error"}
                    break
            print("ENVOIE EN COURS ..")
            time.sleep(2)
            # on renvoie les données à la Mission Control
            sender = SocketAdapter()
            sender.dataSender(feedback)
            time.sleep(2)
       
if __name__ == "__main__":
    main()
             