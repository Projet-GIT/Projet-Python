from time import time

liste = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]

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
