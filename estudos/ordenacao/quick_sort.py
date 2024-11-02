def quicksort(lista, inicio, fim):
    if inicio < fim:
        particao = partition(lista, inicio, fim)
        quicksort(lista, inicio, particao - 1)
        quicksort(lista, particao + 1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

lista = [10, 80, 30, 90, 40]
quicksort(lista, 0, 4)
print(lista)

