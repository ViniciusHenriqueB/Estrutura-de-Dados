buracos = []
cont = 0

l, c = map(int, input().split())
parede = []
for i in range(l):
    linha = input()
    parede.append(linha)
    for j in range(c):
        if parede[i][j] == '.':
            buracos.append((i, j))

print(buracos)
