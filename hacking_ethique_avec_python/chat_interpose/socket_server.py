import socket
import time

HOST_IP = "192.168.1.26"
HOST_PORT = 55836
MAX_DATA_SIZE = 1024

s = socket.socket()
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Attente de connexion sur {HOST_IP}, {HOST_PORT}... ")
connection_socket, client_adress = s.accept()
print(f"Connexion établie avec le {HOST_IP}")

while True:
    sender = input('Vous : ')
    connection_socket.sendall(sender.encode())
    print("En attente d'une reponse...")
    data_recues = connection_socket.recv(MAX_DATA_SIZE)
    print(f"Message : {data_recues.decode()}")

    if not data_recues:
        break

print("Deconnexion serveur, veuillez relancer le programme")
s.close()

time.sleep(10)
