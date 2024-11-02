# RESOLUÇÃO COM BUSCA BINÁRIA (merda deu time limit exceded :( ):

# def BinarySearch(list,item):
#     list.sort()
#     if len(list)==0:
#         return False
#     else:
#         midpoint = len(list)//2
#         if list[midpoint] == item:
#             return True
#         elif item > list[midpoint]:
#             return BinarySearch(list[midpoint+1:], item)
#         else:
#             return BinarySearch(list[:midpoint], item)


# def listaincompleta(lincompleta,lcompleta):
#     faltantes = []
#     for num in lcompleta:

#         if BinarySearch(lincompleta,num) == True:
#             lincompleta.remove(num)
            
#         else:
#             faltantes.append(num)
    
#     faltantes = list(set(faltantes))
#     faltantes.sort()
#     return faltantes


def listaincompleta(lincompleta,lcompleta):
    faltantes = []
    for num in lcompleta:
        if num in lincompleta:
            lincompleta.remove(num)
        else:
            faltantes.append(num)
    
    faltantes = list(set(faltantes))
    faltantes.sort()
    return faltantes

n = int(input())
arr = [int(x) for x in input().split()]
m = int(input())
brr = [int(x) for x in input().split()]

print(*listaincompleta(arr,brr))