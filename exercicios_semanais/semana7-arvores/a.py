def soma_ate_v(v):
    soma = 0
    while v != 0:
        soma += v
        v //= 2
    return soma

n = int(input())
for _ in range(n):
    vertice = int(input())
    print(soma_ate_v(vertice))