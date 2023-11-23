from SocketManager import *


# Exemple d'utilisation
if __name__ == "__main__":
    # Le fichier A envoie des données
    data_to_send = {'cmd': 'ZZZDDZZDZDZDSQSQZDZSSZSZ'}
    sender = SocketAdapter()
    sender.dataSender(data_to_send)
