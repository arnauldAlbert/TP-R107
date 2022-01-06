import sys
import os

# variables globales
listedossier = []
listefiles = []
fichier =""

def main(arg):
    if (len(arg) <4):
        print("il manque des arguments \n usage : TP7-exo3 -d répertoire -f fichier")
    else:
        for i in range(len(arg)):
            if arg[i] == "-d":
                if (os.path.exists(arg[i+1])):
                    listedossier.append(arg[i+1])
            elif arg[i] == "-f":
                fichier = arg[i+1]

    if (fichier != "" and len(listedossier)> 0):
        for dos in listedossier:
            recherche(dos,fichier)
        print(listefiles)
    else:
        print("dossier ou fichier manquant")

###
# fonction de recherche dans un dossier
# cette fonction ajoute tous les sous dossier à la liste des dossiers à parcourir et
# remplis la liste des fichiers trouvés avec leur chemin d'accés
###

def recherche(dossier, fichier):
    liste = os.listdir(dossier)
    for fd in liste:
        if os.path.isfile(dossier+"/"+fd) and fd == fichier:
            listefiles.append(dossier+"/"+fd)
        if os.path.isdir(dossier+"/"+fd):
            listedossier.append(dossier+"/"+fd)


if (__name__ == "__main__"):
    main(sys.argv[1:])