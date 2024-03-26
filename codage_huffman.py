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
    '''
    Fonction qui permet de d'écrire un fichier frequence qui contient les caratères suivies de leur frequence
    '''
    liste = creation_alphabet(nom_fichier)
    with open("RENDU FICHIER/"+nom_fichier + "_freq.txt", 'w') as ecriture:
        ecriture.write(str(len(liste))+"\n")
        for frequence,car in liste:
            ecriture.write(str(frequence)+" "+str(car)+"\n")

def frequence_min(arbres):
    '''
    Fonction qui permet de trouver l'indice du caractère le moins fréquent dans une liste d'arbres
    '''
    indice = 0
    frequence = arbres[0].get_root().get_frequence()
    for i in range (len(arbres)):
        if arbres[i].get_root().get_frequence() < frequence :
            indice = i
            frequence = arbres[i].get_root().get_frequence()
    return indice


def creer_arbre(liste_frequence):
    '''
    Fonction qui permet de créer l'arbre de frequence permettant le codage d'huffman
    '''
    arbres=[]
    #transforme la liste de liste en liste d'abres
    for element in liste_frequence:
        arbre=Arbre(node(element[1],element[0]))
        arbres.append(arbre)
    #applique l'algo de huffman qui consiste à traiter les arbres avec la plus petite frequence en premier 
    while len(arbres) > 1:
        t1= arbres[frequence_min(arbres)]
        arbres.remove(t1)
        t2= arbres[frequence_min(arbres)]
        arbres.remove(t2)
        new_t=Arbre(node(t1.get_root().get_frequence()+t2.get_root().get_frequence(),None,t1.get_root(),t2.get_root()))
        arbres.append(new_t)
    return arbres[0]


def code_caracteres(arbre):
    '''
    Fonction qui permet de créer le dictionnaire contenant les caractères et leur code associé depuis un arbre de frequence
    Cette fonction initialise la récurence 
    '''
    dic_code={}
    arbre.code_arbre("",dic_code)
    return dic_code

def encodage(nom_fichier,dic_code):
    '''
    Fonction qui permet d'écrire le nouveau texte codé à l'aide d'un dic_code et du nom_fichier
    '''
    nom_fichier_code="RENDU FICHIER/"+nom_fichier+"_comp.bin"
    nom_fichier ="RENDU FICHIER/"+nom_fichier+".txt"
    res = bitarray()
    with open(nom_fichier, 'r') as lecteur:
        texte = lecteur.read()
        for char in texte:
            res.extend(dic_code[char])
    with open(nom_fichier_code, 'wb') as ecriture:
        res.tofile(ecriture)

def taux_compression(nom_fichier):
    '''
    Fonction qui permet de comparer la taille du fichier codé et la taille du fichier d'origine
    '''
    new_taille = os.path.getsize("c:/Users/eleme/OneDrive/Bureau/PROJ631_1/RENDU FICHIER/"+nom_fichier+"_comp.bin")
    init_taille = os.path.getsize("c:/Users/eleme/OneDrive/Bureau/PROJ631_1/RENDU FICHIER/"+nom_fichier+".txt")
    return("le taux de compression pour le fichier : ",nom_fichier," est de ", 1-new_taille/init_taille)

def moyenne_codage(dic_code,alphabet,nom_fichier):
    '''
    Fonction qui permet d'afficher la longueur moyenne et la longueur moyenne pondéré des caractères codés
    '''
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

def find(dictionary, binaire):
    for car, code in dictionary.items():
        if code == binaire:
            return car
    return None

def decodage(dico_code,nom_fichier):
    nom_fichier_decode = "RENDU FICHIER/"+nom_fichier+"_decode.txt"
    nom_fichier = "RENDU FICHIER/"+nom_fichier+"_comp.bin"
    res=[]
    with open(nom_fichier, "rb") as file:
        binary_data = file.read()
        binary_list = []
        for byte in binary_data:
            binary_list.extend([int(bit) for bit in '{:08b}'.format(byte)])
    temp=""
    for bin in binary_list:
        temp = temp+str(bin)
        if find(dico_code,temp):
            res.append(find(dico_code,temp))
            temp=""
    with open(nom_fichier_decode, 'w') as ecriture:
        for car in res:
            ecriture.write(str(car))
        

def Huffman_code(nom_fichier):
    '''
    Fonction finale qui regroupe toutes les précédentes, elle permet de :
    - ecrire le texte codé
    - afficher le taux de compression
    - afficher la longueur moyenne des caractères codés
    - ecrire un fichier de frequence
    '''
    alphabet = creation_alphabet(nom_fichier)
    arbre = creer_arbre(alphabet)
    dico = code_caracteres(arbre)
    moyenne_codage(dico,alphabet,nom_fichier)
    encodage(nom_fichier,dico)
    print(taux_compression(nom_fichier))
    alphabet_to_fichier(nom_fichier)

def fichier_to_alphabet(nom_fichier):
    res = []
    retour_chariot = False
    nom_fichier = "RENDU FICHIER/"+nom_fichier+"_freq.txt"
    with open(nom_fichier, 'r') as file:
        texte = file.readlines()
        for indice in range (1,len(texte)):
            if texte[indice][0] == "\n":
                retour_chariot=True
            else :
                if retour_chariot:
                    res.append(("\n",int(texte[indice][1:])))
                    retour_chariot =False
                else:
                    res.append((texte[indice][0],int(texte[indice][2:])))
    return res

def Huffman_decode(nom_fichier):
    alphabet = fichier_to_alphabet(nom_fichier)
    arbre = creer_arbre(alphabet)
    dico = code_caracteres(arbre)
    decodage(dico,nom_fichier)


if __name__ == "__main__":
    '''
    Fonction main qui execute huffman pour tous les textes
    '''
    fichiers = ["textesimple","extraitalice","alice"]
    for fichier in fichiers: 
        Huffman_code(fichier)
        Huffman_decode(fichier)
    
    


