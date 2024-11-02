# Wrong Answer

def birthday(num_quadrados, d, m):
    maneiras_de_dividir = 0
    for i in range(len(num_quadrados)-(m-1)):
        soma = num_quadrados[i]
        soma_a_frente = 1

        if soma_a_frente < m:
            soma += num_quadrados[i + soma_a_frente]
            soma_a_frente += 1
        
        if soma == d and soma_a_frente == m:
            maneiras_de_dividir += 1

    return maneiras_de_dividir

quadrados = int(input())
num_quadrados = [int(x) for x in input().split()]
d, m = map(int, input().split())

print(birthday(num_quadrados, d, m))
