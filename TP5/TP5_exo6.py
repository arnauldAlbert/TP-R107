
chaine = input("saisir une chaine de moins de 100 caractères (sinon les derniers ne seront pas pris en compte ")

count = 0
for i in chaine:
    count+=1


print(f"la chaine contient {count} lettres")

count = 0
for i in range(len(chaine)):
    if chaine[i] in {'i','a','e','o','u','y'}:
        count +=1
print (f"la chaine contient {count} voyelles, cela représente {round(count/len(chaine)*100,1)} % du texte")

subchaine='wagon'
place =-1
count = 0
for i in range(len(chaine)):
    if chaine[i:i+len(subchaine)]==subchaine:
        count +=1

i=0;
while i<len(chaine) and place == -1:
    if chaine[i:i + len(subchaine)] == subchaine:
        place = i
    i+=1

# code équivalent mais plus rapide

place2 = chaine.find(subchaine)

print(f"texte trouvé en {place2}")
if (place>0):
    print(f"la chaine {subchaine} est présente dans la phrase à la place {place}")
    print(f"la chaine {subchaine} apparait {count} fois dans le texte")


