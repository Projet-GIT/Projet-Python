import time
import os
import re

INPUT_FOLDER = r'C:\Users\andyh\OneDrive\Bureau\Andy Python\Input_Files' 
OUTPUT_FOLDER = r'C:\Users\andyh\OneDrive\Bureau\Andy Python\Output_Files'

class treatment():                                                                                                                                      #création de la classe treatment
    def __init__(self, files):                                                                                                                          #initialise  la fonction = constructeur
        self.files = files                                                                                                                              #déclaration de self comme le nom des fichiers à trouver
        self.result = re.search("(\d{2}).(\d{2}) (\d{2})-(\d{2})-(\d{4}).", self.files)                                                                 #liste des les occurence trouver dans la regex, (\d{2}) défini le nombre de décimale a prendre en compte
        self.name_dir_date = str(self.result.group(3)) + "-" + str(self.result.group(4)) + "-" + str(self.result.group(5))                              #si besoin de créer le dossier prendres les résultats des groupes cité
        self.name_dir_hours = str(self.result.group(1))                                                                                                 #création du dossier avec les paramètre du groupe 1 seulement
        print(self.name_dir_date)                                                                                                                       #print le nom du dossier créer

    def treatment_text(self):                                                                                                                           #definition d'une fonction  
        if os.path.isdir(OUTPUT_FOLDER + '\\' + self.name_dir_date) == True:                                                                            #si le dossier date existe
            if os.path.isdir(OUTPUT_FOLDER + '\\' + self.name_dir_date + '\\' + self.name_dir_hours) == True:                                           #vérifie le dossier heure existe
                pass                                                                                                                                    #sinon passe son tour
            else:
                self.create_dir(OUTPUT_FOLDER + '\\' + self.name_dir_date + '\\' + self.name_dir_hours)                                                 #si le dossier heure n'existe pas créer le dossier heure
        else:
                self.create_dir(OUTPUT_FOLDER + '\\' + self.name_dir_date)                                                                              #si le dossier date n'existe pas créer suivie de celui avec l'heure 
                self.create_dir(OUTPUT_FOLDER + '\\' + self.name_dir_date + '\\' + self.name_dir_hours)

        self.move_file(INPUT_FOLDER + '\\' + self.files, OUTPUT_FOLDER + '\\' + self.name_dir_date + '\\' + self.name_dir_hours + '\\' + self.files)    #déplace le documents de input dans output avec les chemin précis


    def create_dir(self, path):
        try:                                                    #essais de créer le dossier
            os.mkdir(path)                                      #lance la command mkdir sur le chemin défini 
        except OSError:                                         #Attrape l'erreur avant que le programme ne s'arrête, pour qu'il puisse continuer
            print ("Creation of the directory failed")          #print une error dans le ou le dossier n'as pas pu être créer mais continue de tourné
    
    def move_file(self, file_path, file_dest):                  #définition de la fontion pour déplacer le document     
        os.replace(file_path, file_dest)                        #command qui déplacera le document


#   
# Main
#

if __name__ == "__main__":                                              #Défini le départ du programme
    while 1:                                                            #boucle infini
        if len(os.listdir(INPUT_FOLDER)) > 0:                           #(os.listedir) renvoie une liste de tous les fichier dans un répertoire(len)donne la longeur de la liste
            print(str(len(os.listdir(INPUT_FOLDER))) + " new entries")  #nouveau fichier trouver, check du nombre de fichier, renvoie l'info en chiffre et les cast en str
            for files in os.listdir(INPUT_FOLDER):                      #création d'un itérateur "file"
                print(files)                                            #print du nom des fichier
                parser = treatment(files)                               #déclaration de parser comme la classe treatment
                parser.treatment_text()
        else:
            print("No new entries")                                     #si aucune entrée trouver renoie cette information
        time.sleep(30)                                                  #si rien trouver après le else arrête pendant 30sec
