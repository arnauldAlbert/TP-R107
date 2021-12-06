note=[]
for i in range (5):
    msg = input(f"veuillez entrer la note du module {i} et le ocefficient correspondant : ")
    note.append(msg.split (" "))
somme=0
msg = "\n"
coeff = 0
valid = True
for i in range(5):
    if float(note[i][0]) < 8 :
        valid =False
        msg += f"Note {i} < 8 \n"
    somme += float(note[i][0])*float(note[i][1])
    coeff += float(note[i][1])

somme = somme/coeff
if (somme < 10):
    valid = False
    msg += f"Moyenne {somme:.2f}< 10 \n"

if valid == True:
    print(f"vous avez validé votre année avec la moyenne {somme:.2f}")
else:
    print(f"vous n'avez pas validé votre année avec les problème suivants {msg}")
