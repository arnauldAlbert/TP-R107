# élément le plus fréquent dans une liste

#remplissage aléatoire d'une liste
from random import randint

liste = [1,1,5,3,5,8,9,0,5,3,8,9,17,2,7,12,3,8]

for i in range(100):
    liste.append(randint(0,20))

max=0
nmax=0

for j in range(len(liste)):
    n=0
    for i in range(len(liste)):
        if (liste[j]==liste[i]):
            n+=1
    if n>nmax:
        nmax = n
        max = j

print(f"L'élément le plus présent est {liste[max]} qui apparait {nmax} fois")