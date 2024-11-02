# OBS.: ÁRVORES SÃO GRAFOS NÃO-DIRIGIDOS, CONEXOS E ACÍCLICOS!

'''
PROPRIEDADES IMPORTANTES

1. Árvores são hierarquias - camadas com informações mais gerais perto da
parte superior e informações mais específicas na parte inferior.

2. Todos os filhos de um nó são independentes dos filhos de outro nó.

3. Cada nó folha é único.

4. Outra propriedade importante das árvores, derivada de sua natureza hierárquica, é que você pode mover seções inteiras de uma árvore (chamada de subárvore ) para uma posição diferente na árvore sem afetar os níveis mais baixos da hierarquia.
'''

'''
VOCABULÁRIO E DEFINIÇÕES

nó - Um nó é uma parte fundamental de uma árvore. Ele pode ter um nome, que chamamos de “chave”. Um nó também pode ter informações adicionais.

aresta - Uma aresta conecta dois nós para mostrar que há um relacionamento entre eles. Cada nó (exceto a raiz) é conectado por exatamente uma aresta de entrada de outro nó. Cada nó pode ter várias arestas de saída. 

raiz - A raiz da árvore é o único nó na árvore que não tem arestas de entrada (o nó inicial).

caminho- Um caminho é uma lista ordenada de nós que são conectados por arestas.

filho - O conjunto de nós c que têm arestas de entrada do mesmo nó são chamados de filhos daquele nó.

pai - Um nó é o pai de todos os nós aos quais ele se conecta com arestas de saída. 

irmão - Os nós na árvore que são filhos do mesmo pai são chamados de irmãos.

subárvore - Uma subárvore é um conjunto de nós e arestas composto por um pai e todos os descendentes desse pai.

nó folha - Um nó folha é um nó que não tem filhos (os nós finais, como as folhas de uma árvore real).

nível - O nível n de um nó é o número de arestas no caminho do nó raiz para n (o nível do nó raiz é 0)

altura - A altura de uma árvore é igual ao nível máximo de qualquer nó na árvore.
'''

'''
DEFINIÇÃO 1 - FORMAL

Uma árvore consiste em um conjunto de nós e um conjunto de arestas que conectam pares de nós. Uma árvore tem as seguintes propriedades:

- Um nó da árvore é designado como nó raiz.

- Cada nó n, exceto o nó raiz, é conectado por uma aresta de exatamente um outro nó p, onde p é o pai de n.

- Um caminho exclusivo atravessa da raiz até cada nó.

- Se cada nó na árvore tem no máximo dois filhos, dizemos que a árvore é uma árvore binária .
'''