class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def filacetamol(string):
    fila =  Queue()
    saida = ''
    for caractere in string:
        if caractere == '*' and not fila.isEmpty():
            saida += fila.dequeue()
        else:
            fila.enqueue(caractere)

    return saida


string = input()
print(filacetamol(string))
