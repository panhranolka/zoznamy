def ktory_min(z:list)->int:
    index = 0
    for i in range(len(z)):
        if z[i] < z[index]:
            index = i
    return index

print(ktory_min([4, 1, 5, 27, -7, 12]))