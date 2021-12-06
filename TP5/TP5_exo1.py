nom1 = input("saisir le nom de la première personne ")
prenom1 = input("saisir le prénom de la première personne ")
nom2 = input("saisir le nom de la seconde personne ")
prenom2 = input("saisir le prénom de la seconde personne ")

if (nom1 < nom2) or (nom1==nom2 and prenom1 < prenom2):
    print(f"personne 1 : {str.capitalize(prenom1)} {str.upper(nom1)}")
    print(f"personne 2 : {str.capitalize(prenom2)} {str.upper(nom2)}")
else:
    print(f"personne 1 : {str.capitalize(prenom2)} {str.upper(nom2)}")
    print(f"personne 2 : {str.capitalize(prenom1)} {str.upper(nom1)}")

