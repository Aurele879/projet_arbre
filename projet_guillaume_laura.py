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
        if self.liste_fils == [] :
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
        if len(self.liste_fils) > 2 :
            return False
        else :
            for fils in self.liste_fils:
                if not fils.binaire:
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
                fil.entrer(fils)
        return liste        

    def affiche(self):
        arbre = Graph()
        print(self.liste_aretes())
        arbre.edges(self.liste_aretes())
        arbre.render(view = True)

    def ajoute_position(self, nom_noeud, fils):
        fil = Fil()
        fil.entrer(self)
        
        while not fil.vide():
            courant = fil.sortir()
            if courant.nom_racine == nom_noeud:
                courant.ajoute_fils(fils)
                return  
            for enfant in courant.liste_fils:
                fil.entrer(enfant)
            
    def parcours_suffixe_supprime(self, nom_noeud):

        def supprimer_recursivement(noeud, parent=None):
            for fils in noeud.liste_fils[:]:  
                supprimer_recursivement(fils, noeud)
            if noeud.nom_racine == nom_noeud and parent != None:
                parent.liste_fils.remove(noeud)
        if self.nom_racine == nom_noeud:
            raise ValueError("Impossible de supprimer la racine de l'arbre.")
        
        supprimer_recursivement(self)
        



root = Arbre(0)
un = Arbre(1)
deux = Arbre(2)
trois = Arbre(3)
quatre = Arbre(4)
cinq = Arbre(5)
root2 = Arbre(6)
sept = Arbre(7)


root.ajoute_fils(un)
root.ajoute_fils(deux)
root.ajoute_fils(trois)
root.ajoute_fils(quatre)
trois.ajoute_fils(cinq)

root2.ajoute_fils(sept)
root.ajoute_position(0, root2)
root.parcours_suffixe_supprime(7)
root.affiche()

print(root.hauteur())
print(root.taille())
print(root.binaire())
print(root.parcours_largeur())
