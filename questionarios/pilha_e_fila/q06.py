# UMA MERDA!

for _ in range(5):
    pilha = True
    fila = True
    prioridade = True
    
    qoperacoes = int(input())
    lista_nums = []
    maior_num = 0
    maiores = []
    for i in range(qoperacoes):
        in_out, num = input().split()
        num = int(num)
        
        if in_out == 'in':
            lista_nums.append(num)
            if num > maior_num:
                maior_num = num
                maiores.append(maior_num)

        else:
            if num == lista_nums[0]:
                if num == maior_num:
                    maiores.pop()
                    if maiores != []:
                        maior_num = maiores[len(maiores) - 1]
                else:
                    prioridade = False

                pilha = False
                lista_nums.pop(0)

            elif num == lista_nums[len(lista_nums) - 1]:
                if num == maior_num:
                    maiores.pop()
                    if maiores != []:
                        maior_num = maiores[len(maiores) - 1]
                else:
                    prioridade = False

                fila = False
                lista_nums.pop()
                
            else:
                fila = False
                pilha = False
                if num != maior_num:
                    prioridade = False
                    lista_nums.remove(num)
                
                else:
                    lista_nums.remove(num)
                    maiores.pop()
                    if maiores != []:
                        maior_num = maiores[len(maiores) - 1]

    if pilha and not fila and not prioridade:
        print('LIFO')
    elif not pilha and fila and not prioridade:
        print('FIFO')
    elif not pilha and not fila and prioridade:
        print('AIPO')
    elif not pilha and not fila and not prioridade:
        print('no hay!')
    else:
        print('uai?')