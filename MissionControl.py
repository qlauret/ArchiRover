import time
from Cartographie import Cartographie
from SocketAdapter import SocketAdapter

class MissionControl:
    def __init__(self, carto: Cartographie):
        self.carto = carto
        # Commande du Rover
        self.cmdAvancer = "Z"
        self.cmdReculer = "S"
        self.cmdTournerDroite = "D"
        self.cmdTournerGauche = "Q"
        self.cmdQuitter = "E"
        
        # Multi-Choix Action
        self.cmdChoixA = "A"
        self.cmdChoixB = "B"

    def launchMission(self):
        print("** BIENVENUE **")
        while True:
            res1 = self.firstInterface()
            self.clearConsole()
            if res1 == self.cmdChoixA:
                print("INSTRUCTIONS ROVER")
                self.roverInterface()
            elif res1 == self.cmdChoixB:
                print("CARTOGRAPHIE")
                self.cartographieInterface()
            elif res1 == self.cmdQuitter:
                self.exitProgramm("TERMINE !")
            else:
                self.exitProgramm("FIN PROGRAMME")

    def waitingResponseTest(self):
        roverResponseBool = False
        cpt = 0  # À ENLEVER
        waiting_string = "ATTENTE DE REPONSE DU ROVER"
        while not roverResponseBool:
            self.clearConsole()
            waiting_string += " ."
            print(waiting_string)
            time.sleep(1)

            if cpt > 2:  # À MODIFIER AVEC LA RÉPONSE DU SOCKET
                roverResponseBool = True
            cpt += 1

        responseString = "0,1,N|0,2,N|0,3,N|0,3,E|1,3,E,X|0,3,E"  # REMPLACER AVEC LA RÉPONSE RÉELLE
        if responseString:
            self.carto.processResponse(responseString)

    def waitingResponse(self):
        receiver = SocketAdapter()
        received_data = receiver.dataReceiver()
        print("Données reçues:", received_data)
        if received_data:
            self.carto.processResponse(received_data)
    
    def roverInterface(self):
        boucle = True
        final_commands = ""
        
        while boucle:
            final_commands = ""
            print("\nDonnez une action au rover:\n * {} : Avancer\n * {} : Reculer\n * {} : Rotation à gauche\n * {} : Rotation à droite".format(
                self.cmdAvancer, self.cmdReculer, self.cmdTournerGauche, self.cmdTournerDroite))
            print(f"ou tapez {self.cmdQuitter} pour annuler les commandes")
            
            user_input = input()
            
            for char in user_input.upper():
                if char == self.cmdAvancer:
                    final_commands += "Z"
                elif char == self.cmdReculer:
                    final_commands += "S"
                elif char == self.cmdTournerDroite:
                    final_commands += "D"
                elif char == self.cmdTournerGauche:
                    final_commands += "Q"
                elif char == self.cmdQuitter:
                    print("ANNULER")
                    final_commands += char.upper()
                else:
                    print(f"\n-- Désolé, la commande {char} n'est pas reconnue. --")
            
            if final_commands and self.cmdQuitter not in final_commands:
                print("ENVOI DES INSTRUCTIONS AU ROVER")
                self.clearConsole()
                data_to_send = {'command': final_commands}
                sender = SocketAdapter()
                sender.dataSender(data_to_send)
                time.sleep(1)
                boucle = False
        
        self.waitingResponse()

    def cartographieInterface(self):
        self.carto.displayCarto()

    def firstInterface(self):
        boucle = True
        choiced = self.cmdQuitter
        while boucle:
            self.clearConsole()
            print(f"Choisissez une action :\n{self.cmdChoixA} : Envoyer instructions au rover\n{self.cmdChoixB} : Voir la cartographie\n{self.cmdQuitter} : Quitter")
            user_input = input()
            
            if len(user_input) == 1:
                if user_input.upper() in [self.cmdChoixA, self.cmdChoixB, self.cmdQuitter]:
                    boucle = False
                    choiced = user_input.upper()
                else:
                    print("Entrez une commande valide")
            else:
                print("Entrez une commande valide")
        
        return choiced

    def exitProgramm(self, message):
        print(message)
        exit(0)

    def clearConsole(self):
        #import os
        #os.system('clear')
        print("\n")
