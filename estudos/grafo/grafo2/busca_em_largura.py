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
    
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'  # AB
        self.distance = 0  # AB
        self.predecessor = None # AB
        
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    # def __str__(self):
    #     return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
    def getColor(self): # AB
        return self.color
    
    def setColor(self, new_color): # AB
        self.color = new_color
    
    def getDistance(self): # AB
        return self.distance
    
    def setDistance(self, new_distance): # AB
        self.distance = new_distance
    
    def getPred(self): # AB
        return self.predecessor
    
    def setPred(self, new_pred): # AB
        self.predecessor = new_pred
        
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    # def __contains__(self,n):
    #     return n in self.vertList

    def addEdge(self,fromm,to,weight=0):
        if fromm not in self.vertList:
            nv = self.addVertex(fromm)
        if to not in self.vertList:
            nv = self.addVertex(to)
        self.vertList[fromm].addNeighbor(self.vertList[to], weight)

    def getVertices(self):
        return self.vertList.keys()

    # def __iter__(self):
    #     return iter(self.vertList.values())

def busca_em_largura(grafo, start):  # "start" é o vértice que começaremos.
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()  # Fila para o vértice de distância k de start seja analisado anter do de distância k + 1
    vertQueue.enqueue(start)

    while vertQueue.size() > 0:   # Este while tem complexidade O(V), onde V é a quantidade de vértices (vertices) no grafo
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections(): # nbr: vizinho  # Este for tem complexidade O(E), onde E é a quantidade de arestas (edges) no grafo
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
            currentVert.setColor('black')

