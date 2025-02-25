# AB -> Usado "Apenas para Busca

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

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    # def __iter__(self):
    #     return iter(self.vertList.values())