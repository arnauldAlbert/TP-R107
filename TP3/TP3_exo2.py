# compte à rebours

n=-1
while n<0:
    n=int(input("saisir un nombre entier positif"))

""" première méthode avec un while """
while n>=0:
    print(n)
    n-=1


""" seconde méthode avec un for """
n=-1
while n<0:
    n=int(input("saisir un nombre entier positif"))

for i in range (n,-1,-1):
    print(i)
