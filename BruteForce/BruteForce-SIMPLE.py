from time import time
import string

liste = string.ascii_letters

def bruteforce(word, length):
    if length <= 5:  #Longueur du mot de passe
        for letter in liste:
            if mdp == word + letter:
                print("Le mot de passe a été trouvé : " + word + letter)
            else:
                bruteforce(word + letter, length + 1)



mdp = input("Entrez votre mot de passe : ")

start = time()
bruteforce('', 1)
end = time()
print('Total time: %.2f seconds' % (end - start))
