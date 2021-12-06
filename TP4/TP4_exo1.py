liste=[]

nombre=float(input("vous cherchez la table de multiplication de quel nombre? "))
for i in range (0,10,1):
    liste.append(i*nombre)

for i in range(0,10,1):
    print(f"{nombre} * {i} = {round(float(liste[i]),1)}")
