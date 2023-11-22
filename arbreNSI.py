class Arbre:
    def __init__(self,valeur):
        self.label = valeur 
        self.G = None
        self.D = None
    
    def est_une_feuille(self):
        if self.G == None and self.D == None:
            return True
        else:
            return False
    
    def setD(self,valeur):
        self.D = valeur
    def setG(self,valeur):
        self.G = valeur
    def getD(self):
        return self.D
    def getG(self):
        return self.G
    def getLabel(self):
        return self.label
    
    def __str__(self):
        if self.est_une_feuille() == True:
            return f"L'arbre n'est qu'une feuille de parent {self.label}"
        else:
            return f"les enfants de {self.label} sont {self.getD()} à droite et {self.getG()} à gauche"

def affichage(ArbreEle):
    if ArbreEle != None:
        return ArbreEle.getLabel() , affichage(ArbreEle.getD()) , affichage(ArbreEle.getG())

MonAbre = Arbre('X')
MonAbre.setD('A')
MonAbre.setG('B')

MonAbre2 = Arbre("X")
print(MonAbre2)
print(MonAbre)

        