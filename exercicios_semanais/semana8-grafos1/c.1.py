import sys
sys.setrecursionlimit(2*(10**5))

class Vertex:
    def __init__(self, id):
        self.id = id
        self.connected_to = []

    def add_neighbor(self, neighbor):
        self.connected_to.append(neighbor)
    
    def get_connections(self):
        return [x.id for x in self.connected_to]
    
    def get_id(self):
        return self.id
    
    
class Graph:
    def __init__(self):
        self.vert_list = {}
    
    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.vert_list:
            return self.vert_list[key]
        else: 
            return None
        
    def add_edge(self, fromm, to):
        if fromm not in self.vert_list:
            self.add_vertex(fromm)
        if to not in self.vert_list:
            self.add_vertex(to)

        self.vert_list[fromm].add_neighbor(self.vert_list[to])

    def get_vertices(self):
        return self.vert_list.keys()


n = int(input())  
grafo = Graph()
for i in range(n):
    repostagem = input().split()
    grafo.add_edge(repostagem[-1].lower(), repostagem[0].lower())
        
polycarp = grafo.get_vertex('polycarp')
conexoes_polycarp = grafo.get_vertex('polycarp').get_connections()
maior_popularidade = [1]

   
def qual_maior_popularidade(cont, conexoes): # Recebe uma lista de adjacentes ao vértice atual (começa com as de Polycarp).
    for conexao in conexoes:
        ultimo_maior = maior_popularidade[len(maior_popularidade) - 1]
        conexoes_da_conexao = grafo.get_vertex(conexao).get_connections()

        if conexoes_da_conexao == []:
            if cont > ultimo_maior:
                maior_popularidade.append(cont)
            
        else:
            qual_maior_popularidade(cont + 1, conexoes_da_conexao)
    
qual_maior_popularidade(2, conexoes_polycarp) # Como n >= 1, comecamos com count = 2
print(maior_popularidade[len(maior_popularidade) - 1])

# for vertice in grafo.get_vertices(): # Printando ligações
#     for ligacao in grafo.get_vertex(vertice).get_connections():
#         print(f'({vertice}, {ligacao})')

# Teste desenhado:
# 7
# M rep polycarp
# N rep M
# E rep polycarp
# F rep E
# J rep E
# H rep J
# G rep polycarp