from pile_et_files import Fil
from graphviz import Graph

class Arbre_binaire:
    def __init__(self, nom):
        self.nom = nom
        self.fils_gauche = None
        self.fils_droit = None
    def __repr__(self):
        if self.fils_gauche != None:
            aff_fils_gauche = f"\nfils gauche :\n {self.fils_gauche.__repr__()}"
        else:
            aff_fils_gauche = ""
        if self.fils_droit != None:
            aff_fils_droit = f"\nfils droit : \n { self.fils_droit.__repr__()}"
        else:
            aff_fils_droit = ""
        return f"Racine : {self.nom}  {aff_fils_gauche } {aff_fils_droit}"
        
    def set_fils_gauche(self, arbre):
        self.fils_gauche = arbre
        
    def set_fils_droit(self, arbre):
        self.fils_droit = arbre

    def taille(self):
        result = 1
        if self.fils_gauche != None:
            result += self.fils_gauche.taille()
        if self.fils_droit != None:
            result += self.fils_droit.taille()
        return result
    
    def feuille(self):
        return self.fils_gauche == None and self.fils_droit == None

    def liste_aretes(self):
        liste = []
        if self.fils_gauche != None:
            liste.append((str(self.nom), str(self.fils_gauche.nom)))
            liste += self.fils_gauche.liste_aretes()
        if self.fils_droit != None:
            liste.append((str(self.nom), str(self.fils_droit.nom)))
            liste += self.fils_droit.liste_aretes()
        return liste

    def liste_feuille(self):
        liste = []
        if self == None:
            return []
        else:
            if self.fils_gauche != None:
                liste += self.fils_gauche.liste_feuille()
            if self.fils_droit != None:
                liste += self.fils_droit.liste_feuille()
            if self.feuille():
                liste.append(self.nom)
        return liste

    
    def parcours_largeur(self):
        liste = []
        fil = Fil()
        fil.entrer(self)
        while not fil.vide():
            self = fil.sortir()
            liste.append(self.nom)
            if self.fils_gauche != None:
                fil.entrer(self.fils_gauche)
            if self.fils_droit != None:
                fil.entrer(self.fils_droit)
        return liste

    def parcours_profondeur1(self):
        liste = []
        liste.append(self.nom)
        if self == None:
            return []
        else:
            if self.fils_gauche != None:
                liste += self.fils_gauche.parcours_profondeur1()
            if self.fils_droit != None:
                liste += self.fils_droit.parcours_profondeur1()
        return liste

    def parcours_profondeur2(self):
        liste = []
        if self.fils_gauche != None:
            liste += self.fils_gauche.parcours_profondeur2()
        liste.append(self.nom)
        if self.fils_droit != None:
            liste += self.fils_droit.parcours_profondeur2()
        return liste

    def parcours_profondeur3(self):
        liste = []
        if self == None:
            return []
        else:
            if self.fils_gauche != None:
                liste += self.fils_gauche.parcours_profondeur3()
            if self.fils_droit != None:
                liste += self.fils_droit.parcours_profondeur3()
            liste.append(self.nom)
        return liste
    
    def affiche(self):
        arbre = Graph()
        print(self.liste_aretes())
        arbre.edges(self.liste_aretes())
        arbre.render(view = True)

        
    def insertion_el_arbre(self, val):
        if val == self.nom:
            return 
        if val <self.nom:   
            if self.fils_gauche == None:
                self.set_fils_gauche(Arbre_binaire(val))
            else:
                self.fils_gauche.insertion_el_arbre(val)
        else:
            if self.fils_droit == None:
                self.set_fils_droit(Arbre_binaire(val))
            else:
                self.fils_droit.insertion_el_arbre(val)

     def distance_feuille(self, distance = 0):
        liste = []
        if self.feuille():
            liste.append((self.nom, distance))
            return liste
        if self.fils_gauche != None:
            liste += self.fils_gauche.distance_feuille(distance + 1)
        if self.fils_droit != None:
            liste += self.fils_droit.distance_feuille(distance + 1)
        return liste
    
    
    def longueur_plus_courte_chaine(self):
        if self.feuille():
            return 0
        gauche = 0
        droite = 0
        if self.fils_gauche is not None:
            gauche = 1 + self.fils_gauche.longueur_plus_courte_chaine()
        if self.fils_droit is not None:
            droite = 1 + self.fils_droit.longueur_plus_courte_chaine()
        return min(gauche, droite)      


def arbre2(n):
    zero = Arbre_binaire("0")
    arbre_courant = zero
    for index in range (1, n+1):
        arbre = Arbre_binaire(index)
        arbre_courant.set_fils_gauche(arbre)
        arbre_courant = arbre_courant.fils_gauche
    return zero     

def arbre3(n) :
    zero = Arbre_binaire("0")
    arbre_courant = zero
    for index in range (1, n+1):
        arbre = Arbre_binaire(index)
        if index % 2 != 0:
            arbre_courant.set_fils_gauche(arbre)
            arbre_courant = arbre_courant.fils_gauche
        else:
            arbre_courant.set_fils_droit(arbre)
            arbre_courant = arbre_courant.fils_droit
    return zero                                    


def hauteur(arbre):
    if arbre == None :
        return 1
    else:
        return 1 + max(hauteur(arbre.fils_gauche), hauteur(arbre.fils_droit))

def taille(arbre):
    if arbre == None:
        return 0
    else:
        return 1 + taille(arbre.fils_gauche) + taille(arbre.fils_droit)

def recherche_el_arbre(elt, arbre):
    if arbre == None:
        return False
    if elt == arbre.nom:
        return True
    if elt < arbre.nom:
        return recherche_el_arbre(elt, arbre.fils_gauche)
    else:
        return recherche_el_arbre(elt, arbre.fils_droit)








if __name__ == "__main__":
    ciquante = Arbre_binaire(50)
    trente_deux = Arbre_binaire(32)
    soixante_sept = Arbre_binaire(67)
    dix_sept = Arbre_binaire(17)
    quarante_trois = Arbre_binaire(43)
    soixante_et_un = Arbre_binaire(61)
    quatre_vingt_trois = Arbre_binaire(83)
    six = Arbre_binaire(6)
    vingt_quatre = Arbre_binaire(24)
    ciquante_trois = Arbre_binaire(53)
    soixante_cinq = Arbre_binaire(65)
    soixante_douze = Arbre_binaire(72)
    quatre_vingt_dix_huit = Arbre_binaire(98)


    ciquante.set_fils_gauche(trente_deux)
    ciquante.set_fils_droit(soixante_sept)
    trente_deux.set_fils_droit(quarante_trois)
    trente_deux.set_fils_gauche(dix_sept)
    dix_sept.set_fils_droit(vingt_quatre)
    dix_sept.set_fils_gauche(six)
    soixante_sept.set_fils_gauche(soixante_et_un)
    soixante_et_un.set_fils_gauche(ciquante_trois)
    soixante_et_un.set_fils_droit(soixante_cinq)
    soixante_sept.set_fils_droit(quatre_vingt_trois)
    quatre_vingt_trois.set_fils_droit(quatre_vingt_dix_huit)
    quatre_vingt_trois.set_fils_gauche(soixante_douze)

    print(recherche_el_arbre(6, ciquante))
    print(ciquante.insertion_el_arbre(58))
    ciquante.affiche()