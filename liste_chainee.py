class Cellule:
    def __init__(self, valeur, successeur= None):
        self.valeur = valeur
        self.successeur = successeur

class Liste_chainee:
   
    def __init__(self):
        self.debut = None   
        self.fin = None 
        self.taille = 0
        
    def  __len__(self):
        compteur = 0
        cc = self.debut
        while cc != None:
            cc = cc.successeur
            compteur += 1
        return compteur

    def __len__(self):
        return self.taille

    def __repr__(self):
        affichage = ""
        cellule_courante = self.debut
        while cellule_courante != None:
            affichage += str(cellule_courante.valeur) + ' '
            cellule_courante = cellule_courante.successeur
        return affichage

    def ajoute_debut(self, valeur):
        cell = Cellule(valeur, self.debut)
        self.debut = cell  
        self.taille += 1
    
    
    def ajoute_fin(self, val):
        if self.debut != None:
            cc = self.debut
            while cc.successeur != None:
                cc = cc.successeur
            cell = Cellule(val)
            cc.successeur = cell
            self.taille += 1
        else:
            self.ajoute_debut(val)

    def supprime_debut(self):
        if self.debut != None:
            if self.debut.successeur == None:
                self.debut = None
                self.fin = None
            else:
                self.debut = self.debut.successeur
            self.taille -= 1

    def supprime_fin(self):
        if self.debut != None:
            if self.debut.successeur == None:
                self.supprime_debut()
            else:
                cc = self.debut
                while cc.successeur.successeur != None:
                    cc = cc.successeur
                cc.successeur = None
                self.taille -= 1
     
    def __getitem__(self, index):
        if 0 <= index < len(self):
            cc = self.debut
            for i in range(index):
                cc = cc.successeur
            return cc.valeur
        else:
            print("index non valide")

    def get_by_val(self, valeur):
        cc = self.debut 
        liste = []
        if len(self) == 0:
            return None
        else:
            for i in range (len(self)):
                if self[i] == valeur:
                    liste.append(i)
            return liste

    def get_by_val2(self, val):
        compteur = 0
        cc = self.debut
        while cc != None and cc.valeur != val:
            compteur+=1
            cc = cc.successeur
        if cc == None: return None
        else:return compteur


    def suppression(self, index):
        if self.debut != None:
            if index == 0:
                self.supprime_debut()
        else:
            if 0 <= index < len(self):
                for i in range(index-1):
                    cc.successeur = cc.successeur.successeur

    def insertion_index(self, val, index):
        if 0 <= index < len(self):
            cc = self.debut
            for i in range(index):
                cc = cc.successeur
            cell = Cellule(val, cc.successeur)
            cc.successeur = cell
            self.taille+=1

    def suppression_val(self, val):
        index = self.get_by_val2(val)
        if self.debut != None:
            if index == 0:
                self.supprime_debut()
        else:
            if 0 <= index < len(self):
                for i in range(index-1):
                    cc.successeur = cc.successeur.successeur

    def ajoute_fin2(self, valeur):
        cell = Cellule(val, None)
        if self.fin == None :
            self.deb = cell
            self.fin = cell
        else:
            self.fin.successeur = cell
            self.fin = cell


if __name__ == "__main__":
    cell = Cellule("a", None)
    cell2 = Cellule("b", cell)
    liste = Liste_chainee()
    liste.ajoute_debut('f')
    liste.ajoute_debut('e')
    liste.ajoute_debut('d')
    liste.ajoute_debut('c')
    liste.ajoute_debut('b')
    liste.ajoute_debut('a')
    print(liste)
    print(liste.get_by_val2('e'))
    liste.insertion_index('w', 2)
    print(liste)
    liste.suppression_val('b')
    print(liste)

#les opérations en tête de liste ne dependent pas de la longueur de la liste O(1)
#les opérations en fin de liste ont une complexité de l'ordre de le longueur de la liste O(n)