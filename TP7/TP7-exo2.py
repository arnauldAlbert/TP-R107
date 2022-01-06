import sys
import os

def main(arg):
    if (len(arg) <1):
        print("il manque le répertoire à tester")
        return -1
    else:
        if (os.path.exists(arg[0])):
            return 0
        else:
            print ("le dossier n'existe pas")
            return -1

def affiche(dossier):
    os.chdir(dossier)
    listefile = os.listdir(".")
    print(f"le dossier contient {len(listefile)} fichiers ou répertoires")

if (__name__ == "__main__"):
    main(sys.argv[1:])