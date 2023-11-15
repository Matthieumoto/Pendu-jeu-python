from random import randint
import time

liste_mots = ['python', 'girafe', 'banane', 'ordinateur', 'plage', 'voiture', 'éléphant', 'musique', 'forêt', 'soleil']

class Pendu :
    def __init__ (self, lettre):
        lettre = list

    def création():
        lettre = []
        i = randint(0, len(liste_mots))
        mot = liste_mots[i]
        for i in range(len(mot)):
            lettre.append(mot[i])
        print("Nous choisisons un mot au hasard !")
        time.sleep(0.5)
        print("Nous avons trouvez un mot, bonne chance a vous !")
        time.sleep(0.5)
        Pendu.jouer(lettre)

    def jouer(lettre):
        vie = 5 - 1
        mauvaise_lettre = []
        mot = []
        mot.append(lettre[0])
        print("Pour vous aidez voici la longueur du mot [", len(lettre), "lettres ], et sa premiere lettre : ",mot)
        print("Votre vie : ", vie + 1)
        i = 1
        Gagner = False
        while Gagner is False:
            print("Voici vottre mot : ", mot)
            time.sleep(0.5)
            choix = input("Veuiller donner un lettre : ",)
            if vie != 0:
                if choix == lettre[i]:
                    print("Bon")
                    mot.append(choix)
                    i += 1
                    if lettre == mot:
                        print("Vous avez gagner ! reste de vie : ",vie + 1)
                        time.sleep(0.5)
                        print("Voici votre mot : ",mot)
                        Gagner = True
                else : 
                    vie -= 1
                    print("Faux")
                    mauvaise_lettre.append(choix)
                    time.sleep(0.5)
                    print("Voici les mauvaise lettre : ",mauvaise_lettre)
                    time.sleep(0.5)
                    print("Vous perdez une vie : ", vie + 1)
            else :
                print("Vous avez perdu car vous avez plus de vie ;( ")
                time.sleep(0.5)
                print("Voici votre mot : ",lettre)
                Gagner = True

Pendu.création()
