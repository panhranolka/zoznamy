def maxx(z:list)->list:
    m = z[0]
    for i in range(len(z)):
        if z[i] > m:
            m = z[i]
    return m
print(maxx([4, 1, 5, 27, 7, 12]))