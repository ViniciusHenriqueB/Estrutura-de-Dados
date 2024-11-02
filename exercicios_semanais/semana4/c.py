def TrocasBubbleSort(lista):
    cont = 0
    for passnum in range(len(lista) - 1, 0, -1):
        for i in range(passnum):
            if lista[i] > lista[i + 1]:
                lista[i], list[i + 1] = lista[i+1], lista[i]
                cont += 1
    return cont

q = int(input())
for _ in range(q):
    listsize = int(input())
    list = [int(x) for x in input().split()]
    print(TrocasBubbleSort(list))
