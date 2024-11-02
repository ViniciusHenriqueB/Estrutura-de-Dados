def BalancedSums(list):  
    list.append(0)
    first = 0
    last = len(list)-1

    while first <= last:
        midpoint = (first+last)//2
        somadir = sum(list[midpoint+1:])
        somaesq = sum(list[:midpoint])

        if somadir>somaesq:
            first = midpoint + 1
        elif somaesq>somadir:
            last = midpoint - 1
        else:
            return 'YES'

    return 'NO'
    
qcasos = int(input())

for _ in range(qcasos):
    qlista = int(input())
    lista = [int(x) for x in input().split()]

    print(BalancedSums(lista))