def decodificador(string_codificada):
    saida = ''
    lista_saida = []
    upper = []
    lower = []

    for letra in string_codificada:

        if ord(letra) >= 65 and ord(letra) <= 90:

            if letra != 'B':
                lista_saida.append(letra)
                upper.append(letra)

            elif upper != []:
                for i in range(len(lista_saida) - 1, -1, -1):
                    if ord(lista_saida[i]) >= 65 and ord(lista_saida[i]) <= 90:
                        lista_saida.pop(i)
                        upper.pop()
                        break
        
        elif ord(letra) >= 97 and ord(letra) <= 122:

            if letra != 'b':
                lista_saida.append(letra)
                lower.append(letra)
                
            elif lower != []:
                for i in range(len(lista_saida) - 1, -1, -1):
                    if ord(lista_saida[i]) >= 97 and ord(lista_saida[i]) <= 122:
                        lista_saida.pop(i)
                        lower.pop()
                        break
    for letra in lista_saida:
        saida += letra
    return saida
                 

qtestes = int(input())

for _ in range(qtestes):
    codificada = input()
    print(decodificador(codificada))