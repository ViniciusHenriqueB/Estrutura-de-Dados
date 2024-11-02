def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista[1:] if i <= pivo]
        maiores = [i for i in lista[1:] if i > pivo]

        return quicksort(menores) + [pivo] + quicksort(maiores)

def findmedian(lista):
    crescente = quicksort(lista)
    return crescente[len(crescente)//2]

q = int(input())
array = [int(x) for x in input().split()]
print(findmedian(array))