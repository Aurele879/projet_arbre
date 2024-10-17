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



if __name__ == "__main__":
    arbre = Arbre_binaire("1")
    six = Arbre_binaire("6")
    trois = Arbre_binaire("3")
    arbre.set_fils_gauche(six)
    six.set_fils_gauche(trois)

    print(arbre.taille())


    