from ftplib import FTP, error_perm
import os
import sys
import shutil
import urllib.request as request
from contextlib import closing
import io
import ftplib
import time


ftp_host ='127.0.0.1'
ftp_login = 'ahenry'
ftp_password = '1234'
INPUT_FOLDER = r'C:\Users\andyh\OneDrive\Bureau\Andy Python\Input_Files' 
OUTPUT_FOLDER = r'C:\Users\andyh\OneDrive\Bureau\Andy Python\Output_Files'
ROOT_SERVER = r'0'



def EnvoieFTP(ftp, path, pathdest):                                 #definition du chemin dans lequel on va chercher les docs et celui dans lequel on l'envoie
    for filename in os.listdir(path):                               #defini "filename" comme étant un élément dans lla liste trouver dans path
        localpath = os.path.join(path, filename)                    #concatène le path et le filename
        print(localpath)                                            
        if os.path.isfile(localpath):                               #prend en compte que les fichier 
            print("file to upload")
            print(localpath)
            ftp.storbinary('STOR ' + filename, open(localpath,'rb'))#permet de envoie les fichier
        elif os.path.isdir(localpath):                              #gère la parti dossier
            print('MKDIR', filename)
            try:
                ftp.mkd(filename)                                   #recrée le dossier avec le même nom sur le FTP
            except error_perm as e:
                if not e.args[0].startswith('550'):                 #gère l'erreur 550 du script afin de renvoyer une erreur sans arrêté le code
                    raise
            
            print("CWD", filename)
            print(ftp.pwd())
            print(pathdest)
            ftp.cwd(filename)                                      #Se déplace dans le nouveau répertoire
            EnvoieFTP(ftp, localpath, pathdest)                    #rappel en boucle de la fonction 
            print("CWD", "..")
            ftp.cwd("..")                                          #Une fois les envoies fini reviens a la racine


def downloadFiles(path, destination, ftp):
    try:
        ftp.cwd(path)                                                       #Se deplace dans le dossier choisit
        os.chdir(destination)                                               #Ouvre le répertoire dans lequel on copie les fichiers
        mkdir_p(destination[0:len(destination)-1] + path)                   #
        print("Created: " + destination[0:len(destination)-1] + path)       #print que le fichier a bien été créé
    except OSError:
        print("OS error detected")
    except ftplib.error_perm:
        print("Error: could not change to " + path)                        #affiche qu'il n'as pas pu changer de path
        sys.exit("Ending Application")                                     #ferme l'application

    filelist=ftp.nlst()                                                    #liste les fichier dans ftp.nlst
    interval = 0.5                                                         #definie l'interval de téléchargement 
    for file in filelist:                                                  #definie file comme étant un élement de filelist
        time.sleep(interval)                                               #ce met pause avec la durée définie dans l'interval
        try:
            print(path)                                                    #essais de print le path
            print(file)                                                    #essais de print les files
            ftp.cwd(path + file)                                           #se déplace sur le path la ou les file ce trouve
            downloadFiles(path + file + "\\", destination, ftp)            #essais la fonction dowloadFiles
        except ftplib.error_perm:                                          #exclut l'erreur dans laquelle windwoss ne donne pas la permition
            os.chdir(destination[0:len(destination)-1] + path)             #ouvre le répertoire dans les dossier

            try:
                print(destination + path)                                  #essais de print la destination et le path
                filen = open(os.path.join(destination[0:len(destination)-1] + path, file), "wb")    #concatène de manière avoir le path précis du fichier
                ftp.retrbinary("RETR " + file, filen)                                               #prend le fichier situé sur le FTP et récupère en local
                print("Downloaded: " + file)
            except:
                print("Error: File could not be downloaded " + file)
    return

def mkdir_p(path):                                  #permet de crée des dossier dans le path définie
    try:
        os.makedirs(path)                           #crée le dossier dans le path 
    except OSError as exc:
        if os.path.isdir(path):                     #si le dossier n'as pas été créée renvoie une erreur(surement une erreur de path)
            pass
        else:
            raise

if __name__ == "__main__":
#def Total():
    ftp = FTP(ftp_host, ftp_login, ftp_password)     #Utilise la librairie FTP pour ce connecté
    print(ftp.getwelcome())                          #Print les info FTP
    print(ftp.nlst())                                #renvoie une liste de ce qu'il y a dans le répertoire FTP
    while 42:                                        #instancie une boucle infinie
        directorylist = ftp.nlst()                   #Liste de ftp.nlst
        response = input("Make a choice: 1." + directorylist[1] + " 2. quit \n")     #affichage des différent dossier avec un choix d'input pour chaque dossier
        if (int(response) == 1):                    #Attribution de la valeur que l'utilisateur devras utiliser pour atteintre un dossier ou quitter
            ftp.cwd(directorylist[0])
        elif (int(response) == 2):
            ftp.quit()
            sys.exit(0)                    #eteint la connexion afin de ne pas créée un zombie

        else:
            print("Must be between 1, 2 or 3")
            ftp.quit()                              
            sys.exit(0)
         
        answer = input("Menu: 1.Upload File, 2.Download File, 3.Quit\n") #input attendu 
        if answer == "1":
            EnvoieFTP(ftp, OUTPUT_FOLDER, ROOT_SERVER)      #utilisation du FTP, de la globale
            ftp.cwd("..")
        elif answer == "2":
            downloadFiles("\\" + directorylist[int(response) - 1] + "\\", INPUT_FOLDER, ftp)    #appel de la fontion dowloadfiles, premier parametre = fichier choisit, pour l'enoyer dans la globale defini
            ftp.cwd("\\")
        elif answer == "3":
            print("Ending")
            ftp.quit()
            sys.exit(42)
        else:
            print("Error answer must be between 1, 2 or 3")