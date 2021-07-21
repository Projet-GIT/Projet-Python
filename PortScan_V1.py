# Scanner de ports V1

##Importation de l'objet socket depuis la standard Library
import socket

## Création de l'objet
##AF_INET Pour de Format IPV4
##STREAM Correspond type de connexion TCP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Définition du serveur cible

server = '127.0.0.1' 

def scanport(port):
    try:
        con = s.connect((server,port))  ##Connexion au serveur
        return True
    except:
        return False

for x in range(20,25):          ## test des ports de 20 à 25
    if scanport(x):
        print('Port',x,'ouvert')
    else:
        print('Port',x,'fermé')




