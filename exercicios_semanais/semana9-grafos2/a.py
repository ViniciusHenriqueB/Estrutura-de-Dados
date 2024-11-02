def posso_proteger(campo, l, c):
    saida = ''
    for i in range(l):     
        for j in range(c):
            if campo[i][j] == 'S':
                if campo[i + 1][j] == 'W' or (j != (c - 1) and campo[i][j + 1] == 'W'):
                    print('No')
                    return 
                else:
                    saida += 'S'
            elif campo[i][j] == 'W':
                if campo[i + 1][j] == 'S' or (j != (c - 1) and campo[i][j + 1] == 'S'):
                    print('No')
                    return 
                else:
                    saida += 'W'   
            else:
                saida += 'D'
        saida += '\n'   

    print('Yes')
    print(saida)

l, c = map(int, input().split())
campo = []

for i in range(l):
    linha = input()
    campo.append(linha)
campo.append('.'*c)

posso_proteger(campo, l, c)