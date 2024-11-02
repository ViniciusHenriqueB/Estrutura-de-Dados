class Stack():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    
def pilhacetamol(string):
    pilha = Stack()
    saida = ''

    for caractere in string:
        if caractere == '*' and not pilha.isEmpty():
            saida += pilha.pop()
        else:
            pilha.push(caractere)

    return saida

string = input()
print(pilhacetamol(string))