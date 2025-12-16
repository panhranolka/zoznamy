import random
def generuj(n:int)->list:
    zoz = []
    for i in range(n):
        zoz.append(random.randrange(5,101))
    return zoz
def parne_pozicie(zoz:list)->list:
    z2 = []
    for i in range (len(zoz)):
        if i%2==0:
            z2.append(zoz[i])
    return z2
print (parne_pozicie(generuj(10)))