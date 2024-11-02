def tracinho(lista):
    for dupla in range(len(lista)//2):
        lista[dupla][1] = '-'

def partition(arr, low, high):
    i = low 
    pivot = arr[low][0]
    for j in range(low+1, high+1):
        if arr[j][0] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[low] = arr[low], arr[i]
    return i 

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
    return arr


q = int(input())
lista = []
string = ''

for _ in range(q):
    num,st = input().split()
    num = int(num)
    dupla = []
    dupla.append(num)
    dupla.append(st)
    lista.append(dupla)

tracinho(lista)

for dupla in quicksort(lista, 0, len(lista) - 1):
    string += dupla[1] + ' '

print(string[:-1])


    

