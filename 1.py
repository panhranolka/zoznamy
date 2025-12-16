import random
def generuj(n:int)->list:
    zoz = []
    for i in range(n):
        zoz.append(random.randrange(5,101))
    return zoz
jojo = generuj(10)
print(jojo)

for prvok in jojo:
    print(prvok)

for i in range(len(jojo)):
    print(jojo[i])

for i, prvok in enumerate(jojo):
    print(i, prvok)