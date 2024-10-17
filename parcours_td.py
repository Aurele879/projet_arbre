from pile_et_files import Fil
from implementation_td import Arbre_binaire
        
        
        
        
def parcours_largeur(arbre):
    liste = []
    fil = Fil()
    fil.entrer(arbre)
    while not fil.vide():
        arbre = fil.sortir()
        liste.append(arbre.nom)
        if arbre.fils_gauche != None:
            fil.entrer(arbre.fils_gauche)
        if arbre.fils_droit != None:
            fil.entrer(arbre.fils_droit)
    return liste

def parcours_profondeur1(arbre):
    liste = []
    liste.append(arbre.nom)
    if arbre == None:
        return []
    else:
        if arbre.fils_gauche != None:
            liste += parcours_profondeur1(arbre.fils_gauche)
        if arbre.fils_droit != None:
            liste += parcours_profondeur1(arbre.fils_droit)
    return liste

def parcours_profondeur2(arbre):
    liste = []
    if arbre == None:
        return []
    else:
        if arbre.fils_gauche != None:
            liste += parcours_profondeur2(arbre.fils_gauche)
            liste += (arbre.fils_gauche.nom)
        liste.append(arbre.nom)
        if arbre.fils_droit != None:
            liste += parcours_profondeur2(arbre.fils_droit)
            liste += (arbre.fils_droit.nom)
    return liste




            




root = Arbre_binaire("root")
a = Arbre_binaire("a")
b = Arbre_binaire("b")
c = Arbre_binaire("c")
d = Arbre_binaire("d")
e = Arbre_binaire("e")
f = Arbre_binaire("f")
g = Arbre_binaire("g")

root.set_fils_droit(b)
root.set_fils_gauche(a)
a.set_fils_droit(d)
a.set_fils_gauche(c)
b.set_fils_droit(f)
b.set_fils_gauche(e)
e.set_fils_droit(g)

print(parcours_profondeur2(root))
