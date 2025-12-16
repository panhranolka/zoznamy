def je_usp(z:list)->bool:
    for i in range(len(z)-1):
        if z[i] > z[i+1]:
            return False
    return True
print(je_usp([1,5,7,12]))
print(je_usp([4,1,5,2,7,12]))