# Preorder (Pré-ordem)- Em uma travessia de preorder, visitamos primeiro o nó raiz e, em seguida, fazemos recursivamente uma travessia de preorder da subárvore esquerda, seguida por uma travessia de preorder recursiva da subárvore direita (nó pai->filho esquerdo->filho direito).
def preorder(tree):
    if tree:  # Se existe uma árvore... (if tree != None...)
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

# Inorder (Em ordem)- Em uma travessia inorder, fazemos recursivamente uma travessia inorder na subárvore esquerda, visitamos o nó raiz e, finalmente, fazemos uma travessia inorder recursiva na subárvore direita (filho esquerdo->nó pai->filho direito).
def inorder(tree):
  if tree:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

# Postorder (Pós-ordem)- Em uma travessia postorder, fazemos recursivamente uma travessia postorder da subárvore esquerda e da subárvore direita, seguida por uma visita ao nó raiz (filho esquerdo->filho direito->nó pai)
def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())