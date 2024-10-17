from liste_chainee import Liste_chainee

class Pile:
    def __init__(self):
        self.donnees =Liste_chainee()  

    def __repr__(self):
        return self.donnees.__repr__()

    def push(self, element):
        self.donnees.ajoute_debut(element)

    def pop(self):
        if self.donnees.debut != None:
            valeur = self.donnees.debut.valeur
            self.donnees.supprime_debut()
            return valeur
        else:
            return None

    def pop2(self):
        if self.vide():
            print("La pile est vide")
        else:
            return self.pop()

    def top(self):
        if self.donnees.debut != None:
            return self.donnee.debut.valeur
    
    def pop3(self):
        self.donnees.supprime_debut()


    def vide(self):
        return self.donnees.debut == None

class Fil:
     
    def __init__(self):
        self.donnee = Liste_chainee()

    def entrer(self, val):
        self.donnee.ajoute_fin(val)

    def sortir(self):
        val = self.donnee.debut.valeur
        self.donnee.supprime_debut()
        return val

    def vide(self):
        return self.donnee.debut == None

    
    def __repr__(self):
        return self.donnee.__repr__()
        

if __name__ == "__main__":
    pile = Pile()
    pile.push(3)
    pile.push(5)
    pile.push(6)
    print(pile)
    print(pile.pop2())
    print(pile.pop3())



