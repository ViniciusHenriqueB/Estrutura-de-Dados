import sys
sys.setrecursionlimit(2000)

def gcd(x,y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x % y)

def findY(x, y, lista):   
    if y >= 1:
        atual = gcd(x, y) + y
        par = [y, atual]
        if len(lista) == 0:
            lista.append(par)
        elif atual > lista[len(lista) - 1][1]:
            lista.append(par)

        return findY(x, y - 1, lista)

qcasos = int(input())
for _ in range(qcasos):
    x = int(input())
    lista = []
    findY(x, x - 1, lista)
    print(lista[len(lista) - 1][0])
    