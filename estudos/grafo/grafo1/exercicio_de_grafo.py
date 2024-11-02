class ExercicioGrafo:
    def todos_os_caminhos_para_o_alvo(self, graph: list[list[int]]):
        # lista de todos os caminhos
        caminhos = []

        # Função recursiva que vai percorrer o grafo
        def procurar_alvo(graph, vertice_atual, vertice_final, caminho_atual):
            # Copia o caminho feito ate agora (evita a perda de informacao durante as chamadas recursivas)
            caminho_atual = caminho_atual.copy()

            # Adiciona o vertice atual
            caminho_atual.append(vertice_atual)

            # Se chegamos ao destino, adicionamos o caminho feito, e retornamos
            if vertice_atual == vertice_final:
                caminhos.append(caminho_atual)
                return
            else:
                # Vizinhos do vertice atual
                for adjacente in graph[vertice_atual]:
                    procurar_alvo(graph, adjacente, vertice_final, caminho_atual)

        procurar_alvo(graph, 0, len(graph) - 1, [])
        return caminhos

garfo = [[1, 2], [3], [3], []]
exercicio_garfo = ExercicioGrafo()

print(exercicio_garfo.todos_os_caminhos_para_o_alvo(garfo))