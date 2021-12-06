chaine = str.lower(input("saisir un mot, une phrase à tester en palindrome : "))

chaine2=""

for i in range(len(chaine)):
    if chaine[i].isalpha():
        chaine2+=chaine[i]

print(chaine2)
i = 0
while (i<len(chaine2)/2-1 and chaine2[i]==chaine2[len(chaine2)-1-i]):
    i+=1

if (i < len(chaine2)/2-1):
    print("ce n'est pas un palindrome")
else:
    print("c'est un palindrome")


