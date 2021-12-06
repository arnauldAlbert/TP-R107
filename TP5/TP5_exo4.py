somme = int(input("saisir une somme d'argent à décomposer"))

nb100 = int(somme/100)
reste = somme%100
nb50 = int(reste/50)
reste = reste % 50
nb10 = int(reste/10)
reste = reste % 10
nb2  = int(reste/2)
nb1 = reste % 2

print(f"{somme} euros, c'est donc {nb100} billets de 100, {nb50} billet de 50, {nb10} billet(s) de 10 {nb2} pièces de 2 et {nb1} pièce de 1")
