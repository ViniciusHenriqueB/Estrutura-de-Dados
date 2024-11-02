# Um grafo pode ser representado por G, onde G = (V, E), onde V é um conjunto de vértices (Vertices) e E é um caminho de arestas (Edges).

# Os objetos são os vértices (ou nós) do grafo.
# Os relacionamentos são as suas arestas.

# Cada aresta pode ser represenrada por uma tupla (u, v) onde u, v pertencem a V (conjunto de vértices).
# Podemos adicionar um terceiro componente à tupla da aresta para representar o peso.

# Grafos podem ser:
'''
Dirigidos: 
- Todas as arestas do grafo possuem uma direção (são unidirecionais), ou seja, na tupla de aresta (u, v), temos que a aresta vai de u para v, mas não vai de v para u. Neste caso dizemos que v é ADJACENTE à u, mas u não é adjacente à v. 

- NESTE TIPO DE GRAFO, PODEMOS TER UMA ARESTA QUE LIGA O VÉRTICE COM ELE MESMO, OS CHAMADOS SELF-LOOPS (OU AUTO-LAÇOS).

- Em grafos dirigidos, o grau de um vértice é o número de arestas que saem do vértice mais o número de arestas que chegam nele.

- O grau do grafo é o grau do vértice de maior grau do grafo.

- Um grafo dirigido é fortemente conexo se há um caminho entre qualquer par de vértices no grafo

- Um grafo dirigido é conexo se possuir um caminho de u para v, ou de v para u para cada par de vértices (u, v)
'''


'''
Não dirigidos (ou não direcionados): 
- As arestas são bidirecionais, logo, temos que (u, v) é o mesmo de (v, u), onde v é adjacente à u e u é adjacente à v. 

- OBS.: NESTE TIPO DE GRAFO NÃO PODEMOS TER SELF-LOOPS (OU AUTO-LAÇOS).

- Em grafos não-dirigidos, o grau de um vértice é o número de arestas que incidem nele.

- O grau do grafo é o grau do vértice de maior grau do grafo.

- Um grafo não dirigido é conexo se cada par de vértices nele estiver conectado por um caminho

- Um grafo dirigido é fracamente conexo se ele não satisfaz os últimos dois tópicos, mas não possui um vértice  isolado (sem arestas saindo ou chegando nele)
'''


# Um caminho de um vértice x a um vérice y é uma sequência de vértices em que, para cada vértice, do primeiro ao penúltimo, há uma aresta ligando esse vértice ao próximo na sequência.

# Um ciclo acontece quando, a partir de determinado vértice, pudermos percorrer algum caminho que nos leve a esse mesmo vértice

# Grafos que possuem pelo menos um ciclo são chamados de CÍCLICOS
# Grafos que não possuem nenhum ciclo são chamados de ACÍCLICOS
