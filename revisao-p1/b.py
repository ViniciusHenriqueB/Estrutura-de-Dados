qtestes = int(input())

for _ in range(qtestes):
    qcubos, indice_cubo_favorito, qcubos_removidos = map(int, input().split())
    lista_cubos = [int(x) for x in input().split()]

    cubo_favorito = lista_cubos[indice_cubo_favorito - 1]
    
    lista_cubos.sort(reverse= True)

    if qcubos_removidos == len(lista_cubos):
        print('YES')

    elif cubo_favorito > lista_cubos[qcubos_removidos - 1]:
        print('YES')

    elif cubo_favorito < lista_cubos[qcubos_removidos - 1]:
        print('NO')
    
    elif lista_cubos[qcubos_removidos - 1] == lista_cubos[qcubos_removidos] and cubo_favorito == lista_cubos[qcubos_removidos - 1]:
        print('MAYBE')

    elif lista_cubos[qcubos_removidos - 1] != lista_cubos[qcubos_removidos] and cubo_favorito == lista_cubos[qcubos_removidos - 1]:
        print('YES')