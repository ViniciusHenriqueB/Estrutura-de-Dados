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
    

def hotPotato(lista, num_passa_batata):
    circulo = Queue()
    for pessoa in lista:
        circulo.enqueue(pessoa)
    while circulo.size() > 1:
        for i in range(num_passa_batata):
            circulo.enqueue(circulo.dequeue())
        circulo.dequeue()
    return circulo.dequeue()
    

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],2))