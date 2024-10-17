from graphviz import Graph
from pile_et_files import Fil

class Arbre:
    
    def __init__(self, nom_racine):
        self.nom_racine = nom_racine
        self.liste_fils = []

    def ajoute_fils(self, fils):
        self.liste_fils.append(fils)

    def liste_aretes(self):
        liste = []
        for fils in self.liste_fils:
            liste.append((str(self.nom_racine), str(fils.nom_racine)))
            liste += fils.liste_aretes()
        return liste

    def affiche(self):
        arbre = Graph()
        print(self.liste_aretes())
        arbre.edges(self.liste_aretes())
        arbre.render(view = True)


    def hauteur(self):
        if self.liste_fils == []:
            return 1
        else:
            liste = []
            for fils in self.liste_fils:
                liste.append(fils.hauteur())
        return 1 + max(liste)

        
    def taille(self):
        result = 1
        for fils in self.liste_fils:
            if fils != None:
                result += fils.taille()
        return result
        
    def binaire(self):
        if len(self.liste_fils) > 2:
            return False
        else:
            for fils in self.liste_fils:
                if not fils.binaire():
                    return False
            return True

    def parcours_largeur(self):
        liste = []
        fil = Fil()
        fil.entrer(self)
        while not fil.vide():
            self = fil.sortir()
            liste.append(self.nom_racine)
            for fils in self.liste_fils:
                if fils != None:
                    liste += fils.parcours_largeur()
        return liste


ciquante = Arbre(50)
trente_deux = Arbre(32)
soixante_sept = Arbre(67)
dix_sept = Arbre(17)
quarante_trois = Arbre(43)
soixante_et_un = Arbre(61)
quatre_vingt_trois = Arbre(83)

ciquante.ajoute_fils(trente_deux)
ciquante.ajoute_fils(soixante_et_un)
ciquante.ajoute_fils(quarante_trois)
ciquante.ajoute_fils(dix_sept)
ciquante.affiche()
print(ciquante.hauteur())
print(ciquante.taille())
print(ciquante.binaire())
print(ciquante.parcours_largeur())


