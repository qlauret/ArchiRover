
# Exemple d'utilisation
from SocketAdapter import SocketAdapter
import time

if __name__ == "__main__":
    while True:
        feedback_test = {
            "status": False,
            "log_movment": [{"x":2,"y":5,"o":"N"},{"x":2,"y":6,"o":"N"},{"x":2,"y":6,"o":"W"}],
            "last_position": {"x":2,"y":6,"o":"W"},
            "error": { "type":"obstacle", "message":"Obstacle on way !", "obstacle_position": {"x":1,"y":6}}
        }
        # Le fichier B reçoit des données
        time.sleep(2)
        receiver = SocketAdapter()
        received_data = receiver.dataReceiver()
        print("Données reçues:", received_data)
        
        time.sleep(2)
        if received_data:
            data_to_send = {'feedback': feedback_test}
            sender = SocketAdapter()
            sender.dataSender(data_to_send)