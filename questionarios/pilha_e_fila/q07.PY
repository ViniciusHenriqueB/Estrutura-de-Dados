class Stack():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    

pilha_de_roupas = Stack()
qroupas = int(input())
tempo_total = 0

for _ in range(qroupas):
    caracteristicas = []
    tipo, cor, tempo = input().split()
    tempo = int(tempo)
    tempo_total += tempo

    caracteristicas.append(tipo)
    caracteristicas.append(cor)
    caracteristicas.append(tempo)
    
    pilha_de_roupas.push(caracteristicas)

for _ in range(qroupas):
    desempilhado = pilha_de_roupas.pop()
    tipo = desempilhado[0]
    cor = desempilhado[1]

    print(f'Tipo: {tipo}, Cor: {cor}')

print(f'Total de roupas: {qroupas}')
print(f'Total de tempo: {tempo_total}')