def nie_cisla(zoz:list)->str:
    z2= []
    for i in range(len(zoz)):
        if not (type(zoz[i])==int or type(zoz[i])==float):
            z2.append(zoz[i])
    return z2
print (nie_cisla(["kuk", 5, "ahoj", -1, 2.5, 4, None, 7, [2,-12], 8, "servus",11]))