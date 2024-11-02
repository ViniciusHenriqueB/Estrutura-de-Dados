from collections import deque, defaultdict

def min_contacts_to_mussum(n, edges, start, mussum):
    # Criação do grafo como uma lista de adjacência
    graph = defaultdict(list)
    
    for edge in edges:
        id_, A, *neighbors = edge
        for neighbor in neighbors:
            graph[id_].append(neighbor)
            graph[neighbor].append(id_)  # Grafo não dirigido
    
    # Se Mussum é o mesmo que o start
    if start == mussum:
        return 0
    
    # BFS inicialização
    queue = deque([start])
    distances = {start: 0}
    
    while queue:
        current = queue.popleft()
        current_distance = distances[current]
        
        for neighbor in graph[current]:
            if neighbor not in distances:
                distances[neighbor] = current_distance + 1
                if neighbor == mussum:
                    return distances[neighbor]
                queue.append(neighbor)
    
    return "Forevis alonis..."

# Testando com o exemplo fornecido
n = 9
edges = [
    [1, 1, 2],
    [2, 2, 3, 4],
    [3, 3, 2, 5, 6],
    [4, 3, 2, 7, 8],
    [5, 1, 3],
    [6, 1, 3],
    [7, 2, 4, 9],
    [8, 1, 4],
    [9, 1, 7]
]
start, mussum = 1, 9

result = min_contacts_to_mussum(n, edges, start, mussum)
print(result) 