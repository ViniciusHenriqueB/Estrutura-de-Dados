def decodificador(string_codificada):
    string_decodificada = ''
    letras_ordenadas = []
    for letra in string_codificada:
        if letra not in letras_ordenadas:
            letras_ordenadas.append(letra)   
    letras_ordenadas.sort()

    dicionario = {}
    first = 0
    last = len(letras_ordenadas) - 1

    while last >= first:
        dicionario[letras_ordenadas[first]] = letras_ordenadas[last]
        dicionario[letras_ordenadas[last]] = letras_ordenadas[first]
        first += 1
        last -= 1
    
    for letra in string_codificada:
        string_decodificada += dicionario[letra]
        
    return string_decodificada

qtestes = int(input())
for _ in range(qtestes):
    len_codificada = int(input())
    codificada = input()
    print(decodificador(codificada))