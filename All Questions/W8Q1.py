import sys
import heapq

class Node():
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize #sets all distances to max size
        self.visited = False    #sets all nodes to not visited
        self.previous = None    #placeholder for previous
        
    def addAdjacent(self, edge, weight = 0):
        self.adjacent[edge] = weight

    def returnAdjacents(self):
        return(self.adjacent.keys())

    def returnWeight(self, edge):
        return(self.adjacent[edge])

    def addDistance(self, dist):
        self.distance = dist

    def returnDistance(self):
        return(self.distance)

    def addPrev(self, prev):
        self.previous = prev

    def addVisit(self):
        self.visited = True

    def __gt__(self, other): # rich comparison method for x > y used in heap
        return(self.returnDistance() > other.returnDistance())
        
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

def dijkstra(graph, start):
    start.addDistance(0)        #sets start node to have 0 distance

    unvisitedQueue = [(n.returnDistance(),n) for n in graph]    #put distance and node into queue
    heapq.heapify(unvisitedQueue)   #convert into heap

    while (len(unvisitedQueue) != 0):
        uv = heapq.heappop(unvisitedQueue)  #pop lowest weight node
        current = uv[1]
        current.addVisit()  #adds node to visited

        for next in current.adjacent:
            newDistance = current.returnDistance() + current.returnWeight(next) #calculates distance travelled

            if newDistance < next.returnDistance(): # checks if newpath is shorter than old path stored
                next.addDistance(newDistance)
                next.addPrev(current)
                print(newDistance)
            #after visiting node
            while len(unvisitedQueue) != 0:
                heapq.heappop(unvisitedQueue) #pop all nodes
            unvisitedQueue = [(v.returnDistance(),v) for v in graph if not v.visited]   #recalculates unvisited
            heapq.heapify(unvisitedQueue) #rebuild unvisitedQueue

def compilePath(v, path):  #adds the shortest way to get to target, returns list in order traversed
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
gr.addEdge("A", "S", 5)
gr.addEdge("S", "C", 11)
gr.addEdge("S", "G", 4)
gr.addEdge("C", "D", 7)
gr.addEdge("C", "E", 10)
gr.addEdge("C", "F", 4)
gr.addEdge("E", "H", 1)
gr.addEdge("F", "G", 15)
gr.addEdge("G", "H", 8)

dijkstra(gr,gr.nodeDict["A"])
    
target = gr.returnNode("E")
path = [target.id]
print("shortest path from start to target: " + str(compilePath(target, path)))







