def BinarySearch(list, itemfaltante, indicenum):
    if len(list)==0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == itemfaltante:
            indicefaltante = list.index(itemfaltante)
            if indicefaltante != indicenum:
                return True
        elif itemfaltante > list[midpoint]:
            return BinarySearch(list[midpoint+1:], itemfaltante, indicenum)
        else:
            return BinarySearch(list[:midpoint], itemfaltante, indicenum)

def IceCreamParlor(dinheiro,lista):
    indices = []

    for i in range(len(lista)):
        faltante = dinheiro - lista[i]
        indicenum = i
        if BinarySearch(lista, faltante, indicenum) == True:
            indicefaltante = lista.index(faltante)
            if indicefaltante > indicenum:
                indices.append(indicenum+1)
                indices.append(indicefaltante+1)
            else:
                indices.append(indicefaltante+1)
                indices.append(indicenum+1)
            break
    return indices

qcasos = int(input())
for _ in range(qcasos):
    totalparagastar = int(input())
    qsabores = int(input())
    preçossabores = [int(x) for x in input().split()]

    print(*IceCreamParlor(totalparagastar,preçossabores))
