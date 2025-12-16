def spolu_do_retazca(zoz:list)->str:
    z =""
    for i in range(len(zoz)):
        z+=str(zoz[i])
    return z
print (spolu_do_retazca((["ahoj", 12, -3, "kukuk", 6.45, True])))