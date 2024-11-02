class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    # Para adicionar um filho esquerdo à árvore, criaremos um novo objeto de árvore binária e definiremos o leftatributo da raiz para se referir a esse novo objeto.

    def insertLeft(self, newNode):
        if self.leftChild == None:  # Quando não há filho esquerdo, basta adicionar um nó à árvore.
            self.leftChild = BinaryTree(newNode)
        else:  # No segundo caso, inserimos um nó e empurramos o filho existente um nível abaixo na árvore.
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    # Para inserir um filho à direita, usa-se a mesma lógica:
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    # Para completar a definição de uma estrutura de dados de árvore binária simples, escreveremos métodos acessadores para os filhos esquerdo e direito, bem como os valores raiz.
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key
    
#  Observe que tanto os filhos esquerdo quanto direito da raiz são instâncias distintas da BinaryTreeclasse. Como dissemos em nossa definição recursiva original para uma árvore, isso nos permite tratar qualquer filho de uma árvore binária como uma árvore binária em si.

    
# def buildTree():
#     tree = BinaryTree('a')
#     tree.insertLeft('b')
#     tree.getLeftChild().insertRight('d')
#     tree.insertRight('c')
#     tree.getRightChild().insertLeft('e')
#     tree.getRightChild().insertRight('f')
#     return tree

# def preorder(tree):
#     if tree:  # Se existe uma árvore... (if tree != None...)
#         print(tree.getRootVal())
#         preorder(tree.getLeftChild())
#         preorder(tree.getRightChild())

# preorder(buildTree())