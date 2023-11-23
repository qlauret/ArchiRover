from SocketManager import *

# Exemple d'utilisation
if __name__ == "__main__":

    # Le fichier B reçoit des données
    receiver = SocketAdapter()
    received_data = receiver.dataReceiver()
    print("Données reçues:", received_data)
