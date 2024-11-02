def buscabinaria(lista, item):
    low = 0
    high = len(lista) - 1
    found = False
    while low <= high and not found:
        midpoint = (low + high) // 2
        if lista[midpoint] == item:
            found = True
        elif lista[midpoint] < item:
            low = midpoint + 1
        else:
            high = midpoint - 1
    return found
