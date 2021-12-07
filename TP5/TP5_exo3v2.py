"""
autre méthode du palindrome utilisant les slices dans les listes
"""

chaine = input("saisir un mot une phrase à tester")
# suppression des caractères spéciaux (ponctuation et espaces)
chaine=''.join(filter(str.isalnum,chaine)).lower()

# récuparation de la chaine inversée à l'aide des slices à valeurs négatives
chaine2  = chaine[::-1]

print(chaine2)

if chaine == chaine2:
    print ("c'est un palindrome")
else:
    print("ce n'est pas un palindrome")