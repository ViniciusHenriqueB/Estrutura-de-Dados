def merge_sort(vetor):
    if len(vetor) < 2:
        return vetor
    meio = len(vetor) // 2
    esquerda = merge_sort(vetor[:meio])
    direita = merge_sort(vetor[meio:])
    return merge(esquerda, direita)

def merge(esquerda, direita):
    vetor = []
    while esquerda and direita:
        if esquerda[0] <= direita[0]:
            vetor.append(esquerda.pop(0))
        else:
            vetor.append(direita.pop(0))
    if esquerda:
        vetor.extend(esquerda)
    if direita:
        vetor.extend(direita)
    return vetor

lista = [2,5,1,3,0,8,10,51]
merge_sort(lista)
print(merge_sort(lista))