import socket
import time

HOST_IP = "192.168.1.26"
HOST_PORT = 55836
MAX_DATA_SIZE = 1024

s = socket.socket()

print(f"Connexion au serveur {HOST_IP}, sur le port {HOST_PORT}")


def server_connection():
    while True:
        try:
            s.connect((HOST_IP, HOST_PORT))
        except ConnectionRefusedError:
            print("Erreur impossible de se connecter au serveur. Reconnexion...")
            time.sleep(4)
        else:
            print("Connexion établie")
            break


server_connection()

while True:
    print("En attente d'une reponse...")
    data_recues = s.recv(MAX_DATA_SIZE)
    print(f"Message : {data_recues.decode()}")
    sender = input('Vous : ')
    s.sendall(sender.encode())
    if not data_recues:
        break

print("Deconnexion serveur, veuillez relancer le programme")

s.close()