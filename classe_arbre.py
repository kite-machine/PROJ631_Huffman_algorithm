
class Arbre:
    """
    Classe arbre
    """
    def __init__(self,root=None):
        self.root=root

    def get_root(self):
         return self.root
class node:
    """
    Classe node en utilisant la structure de donnée recursive
    Son constructeur prend en parametre une valeur et 0,1,2 node
    """
    def __init__(self,frequence,char = None, gauche = None ,droite = None):
        self.char = char
        self.frequence = frequence
        self.gauche = gauche
        self.droite = droite

    def get_char(self):
         return self.char
    
    def get_frequence(self):
         return self.frequence
    
    def get_gauche(self):
         return self.gauche
    
    def get_droite(self):
         return self.droite