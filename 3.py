def coho_je_viac(z:list)->str:
    p = 0
    n = 0
    for i in range(len(z)):
        if z[i] % 2 == 0:
            p += 1
        else:
            n += 1
    if p > n:
        return "parne"
    elif n > p:
        return "neparne"
    else:
        return "rovnako"
print(coho_je_viac([5,1,2,4,7,8,11]))