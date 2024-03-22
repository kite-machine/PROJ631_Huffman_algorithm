from collections import OrderedDict
from classe_arbre import *

def creation_alphabet(nom_fichier):
    '''
    cette fonction retourne une liste trié selon la frequence et le code ascii des caractère d'un texte donnée en parametre
    input : string
    return : list de tuple
    '''
    nom_fichier ="test/"+nom_fichier
    frequence_caractère = {}
    # Ouvre le fichier spécifié en mode lecture ('r') dans un bloc with, assurant sa fermeture automatique après usage.
    with open(nom_fichier, 'r') as file:
        # Lit tout le contenu du fichier et le stocke dans la variable texte.
        texte = file.read()
        for char in texte:
            # Vérifie si le caractère est déjà présent dans le dictionnaire des fréquences.
            if char in frequence_caractère.keys():
                # Si le caractère existe, incrémente sa fréquence de 1.
                frequence_caractère[char] = frequence_caractère.get(char) + 1
            else:
                # Sinon, initialise sa fréquence à 1.
                frequence_caractère[char] = 1
    # Trie le dictionnaire par ordre alphabétique des clés en utilisant sorted() et crée un objet OrderedDict.
    frequence_caractère = OrderedDict(sorted(frequence_caractère.items(), key=lambda t: t[0]))
    # Trie à nouveau le dictionnaire par ordre croissant des valeurs (fréquences).
    frequence_caractère = sorted(frequence_caractère.items(), key=lambda t: t[1])
    return frequence_caractère


def frequence_min(arbres):
    indice = 0
    frequence = arbres[0].get_root().get_frequence()
    for i in range (len(arbres)):
        if arbres[i].get_root().get_frequence() < frequence :
            indice = i
            frequence = arbres[i].get_root().get_frequence()
    return indice


def creer_arbre(liste_frequence):
    arbres=[]
    for element in liste_frequence:
        arbre=Arbre(node(element[1],element[0]))
        arbres.append(arbre)
    while len(arbres) > 1:
        t1= arbres[frequence_min(arbres)]
        arbres.remove(t1)
        t2= arbres[frequence_min(arbres)]
        arbres.remove(t2)
        new_t=Arbre(node(t1.get_root().get_frequence()+t2.get_root().get_frequence(),None,t1.get_root(),t2.get_root()))
        arbres.append(new_t)
    return arbres[0]


def code_caracteres(arbre):
    dic_code={}
    arbre.code_arbre("",dic_code)
    return dic_code

def encodage(nom_fichier,dic_code):
    nom_fichier_code=nom_fichier+"_code.txt"
    nom_fichier ="test/"+nom_fichier+".txt"
    with open(nom_fichier, 'r') as lecteur:
        with open(nom_fichier_code, 'w') as ecriture:
            texte = lecteur.read()
            for char in texte:
                ecriture.write(dic_code[char])



test = creation_alphabet("textesimple.txt")
dic_test = code_caracteres(creer_arbre(test))
encodage("textesimple",dic_test)



