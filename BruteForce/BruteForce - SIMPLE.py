liste = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

word = input('Entrez votre mot de passe : ')
chn = str()


def recherche(chn,word):
     if chn == word:
            print('Vous avez trouvé le mot de passe qui est',chn)

            
for l in liste:
    chn = l
    recherche(chn,word)

    for l2 in liste:
        chn = l +l2
        recherche(chn,word)
       
        for l3 in liste:
            chn = l + l2 + l3
            recherche(chn,word)

            for l4 in liste:
                chn = l + l2 + l3 + l4
                recherche(chn,word)

                for l5 in liste:
                    chn = l + l2 + l3 + l4 + l5
                    recherche(chn,word)
                
