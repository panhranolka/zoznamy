def zoznam_mocnin(n:int)->list:
    z = []
    for i in range(1, n+1):
        z.append(i*i)
    return z
print (zoznam_mocnin(6))