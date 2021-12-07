import os.path
import datetime

saisie=input("saisir les 2 noms de fichiers")
files=saisie.split(' ')

for f in files:
    if os.path.isfile(f):
        print(f"le fichier {f} est bien présent dans le répertoire")
        date = datetime.datetime.fromtimestamp(os.path.getmtime(f))
        print(f"le fichier a été accédé le {date.strftime('%d/%m/%Y %H:%m:%S')}")
    else:
        print(f"le fichier {f} n'existe pas dans le répertoire")