from collections import *
def creation_alphabet(nom_fichier):
    frequence_caractère = {}
    with open(nom_fichier, 'r') as file:
        texte = file.read()
        for char in texte:
            if char in frequence_caractère.keys():
                frequence_caractère[char]=frequence_caractère.get(char)+1
            else:
                frequence_caractère[char]=1
    file.close()
    frequence_caractère = OrderedDict(sorted(frequence_caractère.items(), key=lambda t:t[0]))
    frequence_caractère = OrderedDict(sorted(frequence_caractère.items(), key=lambda t:t[1]))
    return(frequence_caractère)
        


print(creation_alphabet("test/textesimple.txt"))