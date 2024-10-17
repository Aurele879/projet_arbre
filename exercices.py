from pile_et_files import Fil
from implementation_td import Arbre_binaire



def maximum(arbre):
    maxi = int(arbre.nom)
    if arbre == None:
        return []
    else:
        if arbre.fils_gauche != None:
            maxi = max(maxi, maximum(arbre.fils_gauche))
        if arbre.fils_droit != None:
            maxi = max(maxi, maximum(arbre.fils_droit))
    return maxi
        
def somme_arbre(arbre):
    somme = int(arbre.nom)
    if arbre == None:
        return []
    else:
        if arbre.fils_gauche != None:
            somme += somme_arbre(arbre.fils_gauche)
        if arbre.fils_droit != None:
            somme += somme_arbre(arbre.fils_droit)
    return somme

def parcours_largeur_distance(arbre):
    liste = []
    fil = Fil()
    fil.entrer((arbre, 0))
    while not fil.vide():
        arbre, distance = fil.sortir()
        liste.append((arbre.nom, distance))
        if arbre.fils_gauche != None:
            fil.entrer((arbre.fils_gauche, distance+1))
        if arbre.fils_droit != None:
            fil.entrer((arbre.fils_droit, distance+1))
    return liste

def parcours_profondeur1_distance(arbre, distance = 0):
    liste = []
    liste.append((arbre, distance))
    if arbre == None:
        return []
    else:
        if arbre.fils_gauche != None:
            liste += parcours_profondeur1_distance(arbre.fils_gauche, distance+1)
        if arbre.fils_droit != None:
            liste += parcours_profondeur1_distance(arbre.fils_droit, distance+1)
    return liste

def liste_feuille(arbre):
    if arbre == None:
        return []
    liste = []
    if arbre.fils_gauche is not None:
        liste += liste_feuille(arbre.fils_gauche)
    if arbre.fils_droit is not None:
        liste += liste_feuille(arbre.fils_droit)
    if arbre.feuille():
        liste.append(arbre.nom)
    return liste


def distance_feuille(arbre, distance=0):
    if arbre == None:
        return []
    liste = []
    if arbre.feuille():
        liste.append((arbre.nom, distance))
        return liste
    if arbre.fils_gauche is not None:
        liste += distance_feuille(arbre.fils_gauche, distance + 1)
    if arbre.fils_droit is not None:
        liste += distance_feuille(arbre.fils_droit, distance + 1)
    return liste


def longueur_plus_courte_chaine(arbre):
    if arbre == None:
        return None
    if arbre.feuille():
        return 0
    gauche = longueur_plus_courte_chaine(arbre.fils_gauche)
    droite = longueur_plus_courte_chaine(arbre.fils_droit)
    return 1 + min(gauche, droite)


a = Arbre_binaire("1")
b = Arbre_binaire("2")
c = Arbre_binaire("3")
d = Arbre_binaire("4")
e = Arbre_binaire("5")
f = Arbre_binaire("6")
g = Arbre_binaire("6")


a.set_fils_droit(c)
a.set_fils_gauche(b)
b.set_fils_droit(e)
b.set_fils_gauche(d)
e.set_fils_droit(g)


print(parcours_profondeur1_distance(a))