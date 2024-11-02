class Queue():
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


def tempo_total(lista, f, peso_permitido):
    queue = Queue()
    tempo_total = 0
    i = 1

    for elem in lista:
        queue.enqueue(elem)

    while not queue.isEmpty():
        sai_da_pilha = queue.dequeue()

        if i > f:
            i = 1

        if sai_da_pilha <= peso_permitido:
            if i == 1:
                tempo_total += 5
            else:
                tempo_total += 1

            i += 1
        else:
            if i == 1:
                tempo_total += 10
                queue.enqueue(sai_da_pilha - 2)
            else: 
                tempo_total += 1
                
            i += 1
    return tempo_total

    
total_veiculos, f, peso_total_permitido = map(int, input().split())
pesos_veiculos = [int(x) for x in input().split()]

print(tempo_total(pesos_veiculos, f, peso_total_permitido))