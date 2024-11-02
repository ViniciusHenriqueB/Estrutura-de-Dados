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
    def last(self):
        return self.items[0]
    
pessoas = input().split()
rodadas = int(input())
fila_circular = Queue()
for pessoa in pessoas:
    fila_circular.enqueue(pessoa)

for i in range(rodadas):
    fila_circular.enqueue(fila_circular.dequeue())

print(f'Pessoa da frente: {fila_circular.dequeue()}')
print(f'Pessoa do fim: {fila_circular.last()}')