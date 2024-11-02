n, t = map(int, input().split())
celulas = [int(x) for x in input().split()]  # A1, A2, ... , An-1 (estou em A1)

if 1 + celulas[0] == t:
    encontrado = True
else:
    lista_caminhos = [[1, 1 + celulas[0]]]
    encontrado = False

    for i in range(2, n):
        if len(lista_caminhos) != 0 and i == lista_caminhos[len(lista_caminhos) - 1][1]:
            destino = i + celulas[i - 1]
            caminho_atual = [i, destino]
            lista_caminhos.append(caminho_atual)
            if destino == t:
                encontrado = True
                break
        
if encontrado:
    print('YES')
else:
    print('NO')

'''
8 4
1 2 1 2 1 2 1

              0        1       2       3       4       5      6
caminhos = [(1, 2), (2, 4), (3, 4), (4, 6), (5, 6), (6, 8), (7,8)]   conectam (i, i + Ai)
'''