import sys
import heapq

class Node():
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize                 #sets all distances to "infinite"
        self.visited = False                        #sets all nodes to not visited
        self.previous = None
        
    def addAdjacent(self, edge, weight = 0):
        self.adjacent[edge] = weight

    def addDistance(self, dist):
        self.distance = dist

    def __gt__(self, other):                        #rich comparison method for x > y used in heap
        self.distance > other.distance              #allows storing heap of objects

class graph():
    def __init__(self):
        self.nodeDict = {}
        self.dictlen = len(self.nodeDict.keys())

    def __iter__(self):
        return iter(self.nodeDict.values())
        
    def addNode(self, node):
        newNode = Node(node)
        self.nodeDict[node] = newNode

    def returnNode(self, n):
        if n in self.nodeDict:
            return(self.nodeDict[n])
        else:
            return(None)

    def addEdge(self, edge1, edge2, weight = 0):
        self.nodeDict[edge1].addAdjacent(self.nodeDict[edge2], weight)
        self.nodeDict[edge2].addAdjacent(self.nodeDict[edge1], weight)
''' creates list of shortest past travelled backwards, path must be 
reversed to be in chronological order'''  

def dijkstra(graph, start):
    start.addDistance(0)

    unvisitedQueue = [(n.distance, n) for n in graph if n.visited == False] #creates tuple pair of unvisited nodes
    heapq.heapify(unvisitedQueue)                                           #convert tuple to heap
    
    while (len(unvisitedQueue) != 0):
        unvisited = heapq.heappop(unvisitedQueue)   #pop node and sets it to visited
        current = unvisited[1]
        current.visited = True

        for next in current.adjacent:
            newDistance = current.distance + current.adjacent[next] #calculates new distance travelled

            if newDistance < next.distance: #modify distance travelled through current path
                next.addDistance(newDistance)
                next.previous = current
                #print(str(current.id) + str(newDistance))

            while len(unvisitedQueue) != 0: #empty unvisited queue
                heapq.heappop(unvisitedQueue)
            unvisitedQueue = [(n.distance,n) for n in graph if n.visited == False]  #rebuild unvisited queue
            heapq.heapify(unvisitedQueue)
            continue
            
''' creates list of last path travelled, path must be
reveresed to be in chronological order'''
def compilePath(v, path):
    if v.previous != None:
        path.append(v.previous.id)
        compilePath(v.previous, path)
    return(path[::-1])

gr = graph()
gr.addNode("A")
gr.addNode("B")
gr.addNode("C")
gr.addNode("D")
gr.addNode("E")
gr.addNode("F")
gr.addNode("G")
gr.addNode("H")
gr.addNode("S")

gr.addEdge("A", "B", 3)  
gr.addEdge("A", "S", 2)
gr.addEdge("S", "C", 3)
gr.addEdge("S", "G", 11)
gr.addEdge("C", "D", 7)
gr.addEdge("C", "E", 19)
gr.addEdge("C", "F", 4)
gr.addEdge("E", "H", 1)
gr.addEdge("F", "G", 1)
gr.addEdge("G", "H", 8)

target = gr.returnNode("E")

dijkstra(gr,gr.nodeDict["A"])


path = []
path.append(target.id)

print("shortest path from start to target: " + str(compilePath(target, path)))
