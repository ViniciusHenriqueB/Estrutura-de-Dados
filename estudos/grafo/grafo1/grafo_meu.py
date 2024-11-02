class Vertex:  # Classe do vértice. Cada vértice terá sua descrição de adjacência
    def __init__(self, key):
        self.id = key
        self.connected_to = {}  # Dicionário que lista as adjacências do vértice (chave = vizinho do vértice, valor = peso da adjacência)

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    # def __str__(self):  # Testar o que retorna
    #     return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
    def get_connections(self):
        return self.connected_to.keys()
    
    def get_id(self):
        return self.id
    
    def get_weight(self, neighbor):
        return self.connected_to[neighbor]

class Graph:
    def __init__(self):
        self.vert_list = {} # Dicionário que mapeia nomes de vértices para objetos de vértices.
        self.num_vertices = 0

    def add_vertex(self, key): # Adiciona um novo vértice e retorna o objeto Vertex(key)
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex
    
    def get_vertex(self, key):
        if key in self.vert_list:
            return self.vert_list[key]  # Caso o vértice "key" é uma das chaves do dicionário de vértices, retorna o objeto Vertex(key)
        else:
            return None
    
    # def __contains__(self,n):
    #     return n in self.vert_list

    def add_edge(self, fromm, to, weight=0):
        if fromm not in self.vert_list:
            self.add_vertex(fromm)
        if to not in self.vert_list:
            self.add_vertex(to)
        self.vert_list[fromm].add_neighbor(self.vert_list[to], weight)

    def get_vertices(self):
        return self.vert_list.keys()
    
    
    # def __iter__(self):
    #     return iter(self.vert_list.values())

# Utilizando as classes acima, vamos criar o grafo da Figura 2 de https://panda.ime.usp.br/pythonds/static/pythonds_pt/07-Grafos/VocabularyandDefinitions.html

# grafo = Graph()
# for i in range(6):
#     grafo.add_vertex(i)

# print(grafo.num_vertices)
# print(grafo.vert_list)
# print(grafo.get_vertices())

# grafo.add_edge(0,1,5)
# grafo.add_edge(1,2,4)
# grafo.add_edge(2,3,9)
# grafo.add_edge(3,4,7)
# grafo.add_edge(4,0,1)
# grafo.add_edge(0,5,2)
# grafo.add_edge(5,4,8)
# grafo.add_edge(3,5,3)
# grafo.add_edge(5,2,1)

# # for vertice in grafo:
# #     for w in vertice.get_connections():
# #         print(f'({vertice.get_id()}, {w.get_id()})')

# for vertice in grafo.get_vertices(): # Printando ligações
#     for ligacao in grafo.get_vertex(vertice).get_connections():
#         print(f'({vertice}, {ligacao.get_id()})')

# # Obs: Descomentar códigos para verificar e pesquisar sobre os métodos "duplo underline" comentados        
