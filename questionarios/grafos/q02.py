class Queue:
    def _init_(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

def menor_distancia(vertices, distancias, origem, destino):
    fila = Queue()
    fila.enqueue(origem)
    while fila.size() > 0:
        vertice_atual = fila.dequeue()
        for vizinho in vertices[vertice_atual]: 
            if distancias[vizinho] == 0:
                distancias[vizinho] = distancias[vertice_atual] + 1
                fila.enqueue(vizinho)
    return distancias[destino]

num_vertices = int(input())
vertices = {}
distancias = {}

for _ in range(num_vertices):
    entrada = [int(x) for x in input().split()]
    vertice = entrada[0]
    adjacentes = entrada[2:]  # Pula o ID do vértice e a quantidade de vizinhos
    vertices[vertice] = adjacentes
    distancias[vertice] = 0
    
id_origem, id_destino = map(int, input().split())

r = menor_distancia(vertices, distancias, id_origem, id_destino)
if r == 0:
    print('Forevis alonis...')
else:
    print(r - 1)