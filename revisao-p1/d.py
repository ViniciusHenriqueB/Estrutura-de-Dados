def decodificador(string_codificada):
    saida = ''
    lista_saida = []
    upper = []
    lower = []

    for letra in string_codificada:

        if ord(letra) >= 65 and ord(letra) <= 90:

            if letra != 'B':
                lista_saida.insert(0, letra)
                upper.append(letra)
                last_upper = letra

            elif upper != []:
                lista_saida.remove(last_upper)
                upper.pop()
                if len(upper) == 0:
                    last_upper = None
                else:
                    last_upper = upper[len(upper) - 1]
                
        
        elif ord(letra) >= 97 and ord(letra) <= 122:

            if letra != 'b':
                lista_saida.insert(0, letra)
                lower.append(letra)
                last_lower = letra

            elif lower != []:
                lista_saida.remove(last_lower)
                lower.pop()
                if len(lower) == 0:
                    last_lower = None
                else:
                    last_lower = lower[len(lower) - 1]
    
    for letra in range(len(lista_saida) - 1, -1, -1):
        saida += lista_saida[letra]

    return saida
                 

qtestes = int(input())

for _ in range(qtestes):
    codificada = input()
    print(decodificador(codificada))