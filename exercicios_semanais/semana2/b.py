def DivisibleSumPairs(lista, num):
    count = 0
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if i != j:
                soma = lista[i] + lista[j]
                if soma%num == 0:
                    count += 1
    return count

n, k = map(int, input().split())
lista = [int(x) for x in input().split()]
print(DivisibleSumPairs(lista, k))

