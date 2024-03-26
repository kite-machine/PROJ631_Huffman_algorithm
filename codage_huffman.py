from collections import OrderedDict
from classe_arbre import *
from bitarray import bitarray
import os

def creation_alphabet(nom_fichier):
    '''
    cette fonction retourne une liste trié selon la frequence et le code ascii des caractère d'un texte donnée en parametre
    input : string
    return : list de tuple
    '''
    nom_fichier ="RENDU FICHIER/"+nom_fichier+".txt"
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

def alphabet_to_fichier(nom_fichier):
    liste = creation_alphabet(nom_fichier)
    with open(nom_fichier + "_freq.txt", 'w') as ecriture:
        ecriture.write(str(len(liste))+"\n")
        for frequence,car in liste:
            ecriture.write(str(car)+" "+str(frequence)+"\n")


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
    nom_fichier_code=nom_fichier+"_comp.bin"
    nom_fichier ="RENDU FICHIER/"+nom_fichier+".txt"
    res = bitarray()
    with open(nom_fichier, 'r') as lecteur:
        texte = lecteur.read()
        for char in texte:
            res.extend(dic_code[char])
    with open(nom_fichier_code, 'wb') as ecriture:
        res.tofile(ecriture)

def taux_compression(nom_fichier):
    new_taille = os.path.getsize("c:/Users/eleme/OneDrive/Bureau/PROJ631_1/test/"+fichier+"_comp.bin")
    init_taille = os.path.getsize("c:/Users/eleme/OneDrive/Bureau/PROJ631_1/test/"+fichier+".txt")
    return("le taux de compression pour le fichier : ",fichier," est de ", 1-new_taille/init_taille)

def moyenne_codage(dic_code,alphabet,nom_fichier):
    somme = 0
    for code in dic_code.items():
        somme += len(code[1])
    print("la longueur moyenne des caractères de ",nom_fichier," est : ",somme/len(dic_code), "bits")
    somme = 0
    occurence = 0 
    for code in dic_code.items():
        for temp in alphabet:
            if temp[0] == code[0]:
                somme +=  temp[1]*len(code[1])
                occurence += temp[1]
    print("la longueur moyenne pondéré des caractères de ",nom_fichier," est : ",somme/occurence, "bits")

def Huffman(nom_fichier):
    alphabet = creation_alphabet(nom_fichier)
    arbre = creer_arbre(alphabet)
    dico = code_caracteres(arbre)
    moyenne_codage(dico,alphabet,nom_fichier)
    encodage(nom_fichier,dico)
    print(taux_compression(nom_fichier))
    alphabet_to_fichier(nom_fichier)

if __name__ == "__main__":
    fichiers = ["textesimple","extraitalice","alice"]
    for fichier in fichiers: 
        Huffman(fichier)



