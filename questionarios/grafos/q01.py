vertices, arestas, tipo = input().split()
vertices = int(vertices)
arestas = int(arestas)

matriz_de_adjacência = [[0 for i in range(vertices)] for i in range(vertices)]

for i in range(arestas):
    vi, vj, p = map(int, input().split())
    vi -= 1
    vj -= 1
    matriz_de_adjacência[vi][vj] = p
    if tipo == 'N':
        matriz_de_adjacência[vj][vi] = p

for linha in matriz_de_adjacência:
    saida = ''
    for elem in linha:
        elem = str(elem)
        saida += ' '*(4 - len(elem)) + str(elem)
    print(saida)