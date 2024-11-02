# Resolução por Busca em Largura (BFS)

class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def maior_popularidade(grafo, start, distancias):  # BFS
    fila =  Queue()
    fila.enqueue(start)
    while fila.size() > 0:
        current_vert = fila.dequeue()
        for conexao in grafo[current_vert]:
            distancias[conexao] = distancias[current_vert] + 1
            fila.enqueue(conexao)
    return max(distancias.values())
    
n = int(input())  
grafo = {}
distancias = {}
for i in range(n):
    repostagem = input().split()
    postou = repostagem[-1].lower()
    repostou = repostagem[0].lower()
    if repostou not in grafo:
        grafo[repostou] = []
        distancias[repostou] = 0
    if postou not in grafo:
        grafo[postou] = []
        distancias[postou] = 0
    grafo[postou].append(repostou)

print(maior_popularidade(grafo, 'polycarp', distancias) + 1)