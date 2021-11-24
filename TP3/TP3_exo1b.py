N=-1

while (N<=0):
    N = int(input("saisir un entier positif"))

somme = 0
i=0
while (somme<N):
    i += 1
    somme+=i


print (f"à partir du rang {i} la somme des {i} premiers entiers ({somme}) est supérieure à {N}")