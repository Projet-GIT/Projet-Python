
#!/usr/bin/env python
# Mise en place d'un scanner de port avec sauvegarde Horodatée

##Importation de l'objet socket depuis la standard Library
import socket
# importing datetime module pour enregistrement horodaté
import datetime
# importing Pop Up Window notification via un POP-UP
import pyautogui

server = '127.0.0.1' ## Définition du serveur cible avec l'IP

## Création de l'objet
##AF_INET Pour de Format IPV4
##STREAM Correspond au type de connexion TCP
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

##Ajout de la fonction
def scanport(port):
    try:    ##Gestion des erreurs ou exceptions
        con = s.connect((server,port))  ##Connexion au serveur
        return True
    except:
        return False

##Nom du fichier horodaté
filename=datetime.datetime.now()
  
    # Nom du fichier txt horodaté
    # %H= heure -M=minute d=date m=mois Y=année +.txt pour extension + w=write
try:    
    with open(filename.strftime("%Hh%M %d-%m-%Y")+".txt", "w") as file:
        file.write ("Date : " +str(filename) +"\n") ## écriture dans le fichier
        file.write ('+--------+--------+\n')
        file.write ('|Port    | Etat   |\n')
        file.write ('+--------+--------+\n')
        i = int(input("Entrez un port de début: "))            ## choix des ports en input
        j = int(input("Entrez un port de fin: "))

        for x in range(i,j + 1):          ## test des ports +1 pour incrémentation
            if scanport(x):
                print('Port',x,'ouvert')  ##Print+Write ouvert si true
                file.write("Port  "+str(x)+"  :   ouvert \n") 
            else:
                print('Port',x,'fermé')   ##Print+Write fermé si false
                file.write("Port  "+str(x)+"  :   fermé \n")
##configuration POP UP lors de l'export du fichier
    pyautogui.alert(text='Sauvegarde du fichier terminée', button='OK') 
##Ouverture du fichier + Print
    file = open(filename.strftime("%Hh%M %d-%m-%Y")+".txt", "r")
    print(file.read()) 
except:
    print("Veillez relancer le Scan avec des Ports pris en charge, s'il vous plaît") ## Message d'erreur en cas d'exception
    exit(99)
