def p_n(z:list):
    parne = []
    neparne = []
    for i in range(len(z)):
        if z[i] % 2 == 0:
            parne.append(z[i])
        else:
            neparne.append(z[i])
    return parne, neparne
print(p_n([2,3,5,2,1,4,6,5,3,7]))