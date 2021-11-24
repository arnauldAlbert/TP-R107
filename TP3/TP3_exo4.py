# factorielle

#méthode classique

n=-1
while (n<0):
    n=int(input("saisir un entier positif "))

fact = 1
if n>1:
    for i in range (1,n+1,1):
        fact *= i

print(f"{n}! = {fact}")
""" méthode avec une fonction et la récursivité """
def fact(p):
    f=-1
    if p==0 or p==1:
        f=1
    else:
        f = p*fact(p-1)
    return f

n=-1
while (n<0):
    n=int(input("saisir un entier positif "))

print(f"{n}! = {fact(n)}")