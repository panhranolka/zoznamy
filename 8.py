import math
def ludolf(n:int)->str:
    zoz = []
    for i in range(1, n+1):
        zoz.append(round(math.pi, i))
    return zoz
print(ludolf(6))