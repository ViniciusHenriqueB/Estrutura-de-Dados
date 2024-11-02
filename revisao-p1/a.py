def passouNoDoce(string):
    coordenadas = [0, 0]
    for instrucao in string:
        if instrucao == 'U':
            coordenadas[1] += 1
        elif instrucao == 'R':
            coordenadas[0] += 1
        elif instrucao == 'D':
            coordenadas[1] -= 1
        else:
            coordenadas[0] -= 1

        if coordenadas == [1, 1]:
            return 'YES'
    return 'NO'

qcasos = int(input())
for _ in range(qcasos):
    qinstrucoes = int(input())
    string_instrucoes = input()
    print(passouNoDoce(string_instrucoes))
    