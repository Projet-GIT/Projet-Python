##Importation de l'objet socket depuis la standard Library
import socket
# importing datetime module
import datetime

server = '127.0.0.1' ## Définition du serveur cible
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
## Création de l'objet
##AF_INET Pour de Format IPV4
##STREAM Correspond type de connexion TCP
def scanport(port):
    try:
        con = s.connect((server,port))  ##Connexion au serveur
        return True
    except:
        return False

# datetime.datetime.now() to get 
# current date as filename.
filename=datetime.datetime.now()
  
# create empty file
    # Function creates an empty file
    # %d - date, %B - month, %Y - Year
with open(filename.strftime("%Hh%M %d-%m-%Y")+".txt", "w") as file:
    file.write ("Date : " +str(filename) +"\n")
    file.write ('+--------+--------+\n')
    file.write ('|Port    | Etat   |\n')
    file.write ('+--------+--------+\n')
    
    for x in range(20,25):          ## test des ports de 20 à 25
        if scanport(x):
            print('Port',x,'ouvert')
            file.write("Port  "+str(x)+"  :   ouvert \n")
        else:
            print('Port',x,'fermé')
            file.write("Port  "+str(x)+"  :   fermé \n")
