import random
def generuj(n:int)->list:
    zoz = []
    for i in range(n):
        zoz.append(random.randrange(5,101))
    return zoz
def sucet_parne(z:list)->list:
    a = 0
    for i in range(len(z)):
        if z[i]%2==0:
            a += z[i]
    return a 
print(sucet_parne(generuj(10)))
