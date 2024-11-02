def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista[1:] if i <= pivo]
        maiores = [i for i in lista[1:] if i > pivo]

        return quicksort(menores) + [pivo] + quicksort(maiores)

q = int(input())
lista = []

for _ in range(q):
    num = int(input())
    lista.append(num)

for num in quicksort(lista):
    print(num)

#TIME LIMIT EXCEDED