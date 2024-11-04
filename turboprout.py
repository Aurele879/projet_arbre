import os
from graphviz import Graph
from pf import Fil

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
        arbre.render(view=True)
     
    def hauteur(self):
        if self.liste_fils == []:
            return 1
        else:
            liste = [fils.hauteur() for fils in self.liste_fils]
        return 1 + max(liste)
    
    def taille(self):
        result = 1
        for fils in self.liste_fils:
            if fils is not None:
                result += fils.taille()
        return result
    
    def binaire(self):
        if len(self.liste_fils) > 2:
            return False
        else:
            return all(fils.binaire() for fils in self.liste_fils)

    def parcours_largeur(self):
        liste = []
        fil = Fil()
        fil.entrer(self)
        while not fil.vide():
            courant = fil.sortir()
            liste.append(courant.nom_racine)
            for fils in courant.liste_fils:
                fil.entrer(fils)
        return liste        

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
            if noeud.nom_racine == nom_noeud and parent is not None:
                parent.liste_fils.remove(noeud)
        if self.nom_racine == nom_noeud:
            raise ValueError("Impossible de supprimer la racine de l'arbre.")
        
        supprimer_recursivement(self)

    def generer_arbre_from_path(self, chemin):
        """Génère un arbre à partir du chemin spécifié."""
        if not os.path.isdir(chemin):
            raise ValueError(f"{chemin} n'est pas un dossier valide.")
        
        self.nom_racine = os.path.basename(chemin)  # Définit le nom de la racine
        for element in os.listdir(chemin):
            chemin_complet = os.path.join(chemin, element)
            if os.path.isdir(chemin_complet):
                # Si c'est un dossier, crée un nœud et l'ajoute à l'arbre
                fils = Arbre(element)
                fils.generer_arbre_from_path(chemin_complet)  # Récursion pour le contenu
                self.ajoute_fils(fils)
            else:
                # Si c'est un fichier, crée un nœud et l'ajoute à l'arbre
                fils = Arbre(element)
                self.ajoute_fils(fils)

# Exemple d'utilisation
if __name__ == "__main__":
    chemin = "/home"  # Remplacez par votre chemin
    arbre = Arbre("Racine")
    arbre.generer_arbre_from_path(chemin)
    arbre.affiche()
