import os
import sys
from time import time
from numpy import loadtxt

liste_name = loadtxt('names.txt', dtype=str)
liste_mdp = loadtxt('probable-v2-top12000.txt',dtype=str)

chaine = str()

pseudo = input("Entrez le pseudo : ")
######## Trouver le pseudo ########
def findNAME(chaine,pseudo):
    while(True):
        if chaine == pseudo:
            print("Vous avez trouvez le pseudo ! ")
            break
        else:
            break

################################################
######## Fonction pour trouver l'éléments ####
def brutname():
    for lname in liste_name:
        chaine= lname
        findNAME(chaine,pseudo)  
        # print(chaine) # Affiche la liste des prénoms

start = time()
brutname()
end = time()
print('Total time: %.2f seconds' % (end - start))
################################################

mdp = input("Entrez le mot de passe : ")
######## Trouver le mot de passe ########

def findMOTDEPASSE(chaine,mdp):
    while(len(chaine) > 1): 
        if chaine == mdp:
            print("Vous avez trouvez le mot de passe ! ")
            break
                
        else:
            break
            #print("Le mot de passe n'est pas dans cette liste !")
            

################################################
######## Fonction pour trouver les éléments ####
def brutmdp():
        for lmdp in liste_mdp:
            chaine = lmdp
            findMOTDEPASSE(chaine,mdp)
            #print(chaine) # Affiche la liste des mdp

######## Executable ########
start = time()
brutmdp()
end = time()
print('Total time: %.2f seconds' % (end - start))
