nbheures = int(input("indiquer le nombre d'heures travaillées"))
sh = float(input("donner le taux horaire"))

if nbheures< 160:
    salaire = nbheures * sh
elif nbheures < 200:
    salaire = (160 + (nbheures-160)*1.25)*sh
else:
    salaire = (160 + 40*1.25 + (nbheures-200)*1.5)*sh

print (f"pour {nbheures} travaillées, vous avez gagné {salaire} euros")