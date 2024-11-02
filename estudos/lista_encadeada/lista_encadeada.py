# Vídeo foda: 
# Parte 1 - https://youtu.be/jIM87UqOq3g?si=clXo1d4hjrAZSDH5
# Parte 2 - https://youtu.be/tJGkcSqcPms?si=eqnZz6ZXiSEhk_9A

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
            self._size += 1
        else:
            # primeira inserção
            self.head = Node(elem)
            self._size += 1
    
    def __len__(self): 
        # Retorna o tamanho da lista (permite utilizar a função len())
        return self._size
    
    def _get_node(self, index): # Retorna o nó que está "index"     
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next  
            else:
                raise IndexError('list index out of range')
        return pointer
    # def get(self, index):
        # lista.get(5)
    #     ...
    def __getitem__(self, index):  # Maneira mais pythônica
        # a = Lista[5]
        pointer = self._get_node(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError('list index out of range')

    # def set(self, index, elem):
        # lista.set(5, 2)
    #     ...    
    def __setitem__(self, index, elem):  # Maneira mais pythônica
        # Lista[5] = 2
        pointer = self._get_node(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError('list index out of range')
    
    def index(self, elem): # Se o elem procurado está na lista, a função retorna sua posição
        pointer = self.head
        i = 0
        while(pointer):
            if pointer == elem:
                return 0
            pointer = pointer.next
            i += 1
        raise ValueError(f'{elem} is not in list')
    
    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._get_node(index - 1)
            node.next = pointer.next
            pointer.next = node

        self._size += 1
        
    def remove(self, elem):
        if self.head == None:
            raise ValueError(f'{elem} is not in list')
        elif self.head.data == elem:
            self.head = self.head.next
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size -= 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError(f'{elem} is not in list')
    
    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

                
lista = LinkedList()
lista.append(7)

lista.append(4)
lista.insert(1, 1)
print(lista)