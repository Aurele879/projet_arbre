import os
from graphviz import Graph  # Import pour visualiser l'arbre
from pile_et_files import Fil  # Classe pour la gestion de files

class Arbre:
    
    def __init__(self, nom_racine):
        """Initialise un nœud d'arbre avec un nom et une liste de fils vide."""
        self.nom_racine = nom_racine  # Nom du nœud racine
        self.liste_fils = []  # Liste pour les nœuds enfants

    def ajoute_fils(self, fils):
        """Ajoute un fils (nœud enfant) à la liste de fils du nœud courant."""
        self.liste_fils.append(fils)

    def liste_aretes(self):
        """Génère une liste des arêtes de l'arbre pour chaque connexion parent-enfant."""
        liste = []
        for fils in self.liste_fils:
            # Ajoute une arête entre le nœud courant et chacun de ses fils
            liste.append((str(self.nom_racine), str(fils.nom_racine)))
            # Appel récursif pour récupérer les arêtes des sous-arbres
            liste += fils.liste_aretes()
        return liste
    
    def affiche(self):
        """Affiche une représentation graphique de l'arbre."""
        arbre = Graph()
        print(self.liste_aretes())  # Affiche les arêtes dans la console pour référence
        arbre.edges(self.liste_aretes())  # Passe les arêtes au graphe Graphviz
        arbre.render(view=True)  # Affiche le graphe

    def hauteur(self):
        """Calcule la hauteur de l'arbre (longueur du chemin le plus long vers une feuille)."""
        if self.liste_fils == []:  # Cas de base : un nœud sans fils
            return 1
        else:
            # Calcule la hauteur de chaque sous-arbre et retourne le maximum
            liste = [fils.hauteur() for fils in self.liste_fils]
        return 1 + max(liste)
    
    def taille(self):
        """Calcule le nombre total de nœuds dans l'arbre."""
        result = 1  # Compte le nœud courant
        for fils in self.liste_fils:
            if fils is not None:
                result += fils.taille()  # Ajoute la taille de chaque sous-arbre
        return result
    
    def binaire(self):
        """Vérifie si l'arbre est binaire (chaque nœud a au plus 2 fils)."""
        if len(self.liste_fils) > 2:
            return False
        else:
            # Vérifie récursivement pour tous les fils
            return all(fils.binaire() for fils in self.liste_fils)

    def parcours_largeur(self):
        """Renvoie une liste des noms de nœuds par parcours en largeur."""
        liste = []
        fil = Fil()  # Utilise une file pour gérer les nœuds
        fil.entrer(self)  # Ajoute le nœud racine dans la file
        while not fil.vide():
            courant = fil.sortir()  # Retire un nœud de la file
            liste.append(courant.nom_racine)  # Ajoute le nom du nœud à la liste
            for fils in courant.liste_fils:
                fil.entrer(fils)  # Ajoute les fils dans la file pour parcours en largeur
        return liste        

    def ajoute_position(self, nom_noeud, fils):
        """Ajoute un nœud fils au nœud ayant le nom 'nom_noeud'."""
        fil = Fil()
        fil.entrer(self)  # Démarre à partir de la racine
        while not fil.vide():
            courant = fil.sortir()
            if courant.nom_racine == nom_noeud:
                courant.ajoute_fils(fils)  # Ajoute le fils trouvé
                return  
            for enfant in courant.liste_fils:
                fil.entrer(enfant)  # Explore les nœuds enfants

    def parcours_suffixe_supprime(self, nom_noeud):
        """Supprime un nœud donné (et ses descendants) en utilisant un parcours en suffixe."""
        def supprimer_recursivement(noeud, parent=None):
            for fils in noeud.liste_fils[:]:  # Parcourt copie de liste_fils pour modifier en cours de boucle
                supprimer_recursivement(fils, noeud)  # Récursion pour supprimer descendants
            # Supprime le nœud s'il correspond et qu'il a un parent
            if noeud.nom_racine == nom_noeud and parent != None:
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
    chemin = "/home/mazella/Images"  # Remplacez par votre chemin
    arbre = Arbre("Racine")
    arbre.generer_arbre_from_path(chemin)
    arbre.affiche()
