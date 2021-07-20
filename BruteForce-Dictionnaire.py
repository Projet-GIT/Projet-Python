from time import time
import threading,sys
from numpy import loadtxt

liste_name = loadtxt('names.txt', dtype=str)
liste_mdp = loadtxt('probable-v2-top12000.txt',dtype=str)

chaine = str()

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global queue


def findNAME(chaine,pseudo):
    while(True):
        if chaine == pseudo:
            print("Vous avez trouvez le pseudo ! ")
            break
        else:
            break

def brutname():
    for lname in liste_name:
        chaine = lname
        findNAME(chaine,pseudo)  
        # print(chaine) # Affiche la liste des prénoms


def findMOTDEPASSE(chaine,mdp):
    while(len(chaine) > 1): 
        if chaine == mdp:
            print("Vous avez trouvez le mot de passe ! ")
            break
                
        else:
            break
            #print("Le mot de passe n'est pas dans cette liste !")

def brutmdp():
        for lmdp in liste_mdp:
            chaine = lmdp
            findMOTDEPASSE(chaine,mdp)


MyThread()

start = time()
pseudo = input("Entrez le pseudo : ")
brutname()
mdp = input("Entrez le mot de passe : ")
brutmdp()
end = time()
print('Total time: %.2f seconds' % (end - start))


