import os
import sys

listeRepertoires = []
listeFichiers = []

def aide(msg):
      print(msg)
      print(f"usage {sys.argv[0]} -d répertoire - f fichier") # affiche le nom du script et comment il faut appeler ce script exit
def recherche(repertoire, fichier):
# Lister les fichiers du répertoire en vous plaçant dans celui-ci
    contenuDuRépertoire = os.listdir(repertoire)
    for elt in contenuDuRépertoire : # pour chaque élément (elt) du répertoire
        if os.path.isdir(repertoire+"/"+elt): # si c’est un répertoire
            listeRepertoires.append(repertoire + "/" + elt)
        elif os.path.isfile(repertoire+"/"+elt) : # sinon si c’est un fichier
            if elt == fichier : # si c’est le même de fichier
                listeFichiers.append(repertoire + "/" + elt)

if __name__ == '__main__':
    if len(sys.argv) < 5 : # mauvais nombre d’arguments
        aide("Mauvais nombre d’arguments")
    else:
        repertoire = ""
        fichier = ""
        for i in range(1,len(sys.argv)): # je recherche les arguments
            if sys.argv[i] == "-d":
                repertoire = sys.argv[i+1]
            elif sys.argv[i] == "-f":
                fichier = sys.argv[i+1]
    if os.path.exists(repertoire) == False : # si le repertoire n’existe pas
        aide("répertoire qui n'existe pas")
    else :
        if len(os.listdir(repertoire)) == 0 or fichier == "": # si repertoire ou fichier sont vides
            aide("répertoire ou fichier vide")
        else:
            listeRepertoires.append(repertoire)
            for dos in listeRepertoires:
                recherche(dos, fichier)
            for fiche in listeFichiers :
                print(fiche)
