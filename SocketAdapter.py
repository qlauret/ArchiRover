import pickle
import socket

class SocketAdapter:
    def __init__(self, host='127.0.0.1', port=12345):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def dataSender(self, data):
        try:
            self.socket.connect((self.host, self.port))
            serialized_data = pickle.dumps(data)
            self.socket.sendall(serialized_data)
        finally:
            self.socket.close()

    def dataReceiver(self):
        try:
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            print(f"Attente de la connexion sur {self.host}:{self.port}")
            connection, client_address = self.socket.accept()

            with connection:
                print(f"Connexion établie avec {client_address}")
                received_data = b""
                while True:
                    data = connection.recv(1024)
                    if not data:
                        break
                    received_data += data

                deserialized_data = pickle.loads(received_data)
                return deserialized_data

        finally:
            self.socket.close()