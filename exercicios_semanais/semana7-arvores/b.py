class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self, id):
        child = BinaryTree(id)
        self.leftChild = child
        return child
    def insertRight(self, id):
        child = BinaryTree(id)
        self.rightChild = child
        return child
    def getRootVal(self):
        return self.root

def post_order(tree):
    if tree:
        post_order(tree.leftChild)
        post_order(tree.rightChild)
        print(tree.getRootVal(), end=' ')

def pre_order_em_arvore(root, filhos):
    if filhos:
        filhos_esq = [x for x in filhos if x < root.getRootVal()]
        filhos_dir = [x for x in filhos if x > root.getRootVal()]
        if filhos_esq:
            filho = root.insertLeft(filhos_esq[0])
            pre_order_em_arvore(filho, filhos_esq[1:])
        if filhos_dir:
            filho = root.insertRight(filhos_dir[0])
            pre_order_em_arvore(filho, filhos_dir[1:])

n = int(input())
pre_order = [int(x) for x in input().split()]
root = BinaryTree(pre_order[0])
filhos = pre_order[1:]
pre_order_em_arvore(root, filhos)
post_order(root)
print(root)