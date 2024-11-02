# Nesta classe adicionei o nível de cada nó, que vai incrementando a medida em que os nós são adicionados

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        self.nivel = 0    
    
    # Para adicionar um filho esquerdo à árvore, criaremos um novo objeto de árvore binária e definiremos o leftatributo da raiz para se referir a esse novo objeto.

    def insertLeft(self, newNode):
        if self.leftChild == None:  # Quando não há filho esquerdo, basta adicionar um nó à árvore.
            self.leftChild = BinaryTree(newNode)
            self.leftChild.nivel = self.nivel + 1
        else:  # No segundo caso, inserimos um nó e empurramos o filho existente um nível abaixo na árvore.
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            self.leftChild.nivel = self.nivel + 1
            t.leftChild.nivel = t.nivel + 1
    
    # Para inserir um filho à direita, usa-se a mesma lógica:
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
            self.rightChild.nivel = self.nivel + 1
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            self.rightChild.nivel = self.nivel + 1
            t.rightChild.nivel = t.nivel + 1

    # Para completar a definição de uma estrutura de dados de árvore binária simples, escreveremos métodos acessadores para os filhos esquerdo e direito, bem como os valores raiz.
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key
    
    def getNivel(self):
        return self.nivel


# Função que retorna a altura de um nó:
def altura(no):
    if no == None:
        return -1
    altura_esquerda = altura(no.getLeftChild())
    altura_direita = altura(no.getRightChild())
    if altura_esquerda > altura_direita:
        return altura_esquerda + 1
    return altura_direita + 1

