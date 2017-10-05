import socket

hote = "localhost"
port = 18181

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion established with server on port {}".format(port))

# Le client repond au message HELLO du serveur une fois connecté par un HELLO également
msg_init=connexion_avec_serveur.recv(1024)
print(msg_init.decode())
connexion_avec_serveur.send(msg_init)

msg_a_envoyer = b""
while msg_a_envoyer.upper() != b"QUT":
    msg_a_envoyer = input("> Enter your query : ")
    print("Query : {}".format(msg_a_envoyer.upper()))
    msg_a_envoyer = msg_a_envoyer.encode()
    # On envoie le message au serveur
    connexion_avec_serveur.send(msg_a_envoyer)
    # On lit la reponse du serveur
    msg_recu = connexion_avec_serveur.recv(1024)
    print(msg_recu.decode())

print("Connexion closed")
<<<<<<< HEAD
connexion #Je l'ai modifiée !
=======
connexion_avec_serveur.open()
>>>>>>> dfa79ed37bf6dccaac77c6803f1bd992a311ecab
