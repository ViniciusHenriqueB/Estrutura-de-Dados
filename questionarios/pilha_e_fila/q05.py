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

pilha_de_anilhas = Stack()

while True:
    anilha = int(input())
    if anilha == 0:
        break
    pilha_de_anilhas.push(anilha)

anilha_desejada = int(input())
anilhas_retiradas = 0
peso_total_movimentado = 0

for i in range(pilha_de_anilhas.size()):
    if pilha_de_anilhas.peek() == anilha_desejada:
        peso_encontrado = pilha_de_anilhas.pop()
        anilhas_retiradas += 1
        peso_total_movimentado += peso_encontrado
        print(f'Peso retirado: {peso_encontrado}')
        break
    else:
        peso_retirado = pilha_de_anilhas.pop()
        anilhas_retiradas += 1
        peso_total_movimentado += peso_retirado
        print(f'Peso retirado: {peso_retirado}')

print(f'Anilhas retiradas: {anilhas_retiradas}')
print(f'Peso total movimentado: {peso_total_movimentado}')



