# É possível modificar para pegar o caminho de um nó inicial para um nó qualquer (grafo precisa ser acíclico):

def caminhos_ate_o_alvo(grafo):
    caminhos = []
    
    def caminho(grafo, caminho_atual, vertice_atual, vertice_final):
        caminho_atual = caminho_atual.copy()
        caminho_atual.append(vertice_atual)
        if vertice_atual == vertice_final:
            caminhos.append(caminho_atual)
            return
        for adjacente in grafo[vertice_atual]:
            caminho(grafo, caminho_atual, adjacente, vertice_final)
        
    caminho(grafo, [], 0, len(grafo) - 1)
    return caminhos

# [[4,3,1],[3,2,4],[3],[4],[]]
# grafo =  {0: [4,3,1], 1:[3,2,4], 2: [3], 3: [4], 4: []}
# print(caminhos_ate_o_alvo(grafo))