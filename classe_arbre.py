
class Arbre:
    """
    Classe arbre
    """
    def __init__(self,root=None):
        self.root=root

    def get_root(self):
         return self.root
    
    def get_sub_tree(self):
          """
          primitive retournant une liste de Rtree où la racine et l'un des fils de self
          """
          res=[]
          for noeud in self.get_root().get_children() :
               res.append(Arbre(noeud))
          return res

    def display_depth(self):
          """
          primitive affichant l'arborescence en utilisant le parcours de profondeur
          """
          print(self.get_root().get_char())
          if self.get_root().get_children() != None:
               for arbre in self.get_sub_tree() :
                    arbre.display_depth()

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
    
    def get_children(self):
        """
        primitive retournant la liste des enfants du noeud
        """
        if self.gauche or self.droite :
          return [self.gauche,self.droite]
        else: 
          return None
    
    def get_gauche(self):
         return self.gauche
    
    def get_droite(self):
         return self.droite