class Node():
    def __init__(self, name):
        self.name = name
        self.adjacent = []
        
    def addAdjacent(self, edge):
        self.adjacent.append(edge)
    
class graph():
    
    def __init__(self, nodeDict = {}):
        self.nodeDict = nodeDict 
    
    def addNode(self, node):
        newNode = Node(node)
        self.nodeDict[node] = newNode

    def addEdge(self, edge1, edge2):
        #add a connection of edge1 to edge 2
        self.nodeDict[edge1].addAdjacent(edge2)
        #add a connection of edge2 to edge 1
        self.nodeDict[edge2].addAdjacent(edge1)
        #node connected in a 2 way

    def bfs(self, nod):
        stack = []
        stack.append(nod)
        path = []
        while len(stack) != 0:  
            stack.extend(self.nodeDict[stack[0]].adjacent) #add contents of current node to stack
            if stack[0] not in path:
                path.append(stack.pop(0))   #if node isnt in path list, pop and append to path
            elif stack[0] in path:      #if node is in path, pop node
                stack.pop(0)
            if len(self.nodeDict.keys()) == len(path):  #check if all nodes are in path, return path and break loop
                return(path)
                break


    def dfs(self, dic, nod, path=[]):
        for eachNode in self.nodeDict.keys():
            dic[eachNode] = self.nodeDict[eachNode].adjacent    #make copy of dictionary
        stack = []
        stack.append(nod) #add first node to stack
        while (len(stack) != 0):
            x = stack.pop()     #take of end node from stack
            if x not in path:   
                path += [x]     #add x to path
                stack += dic[x] #add dic[x] to stack
                continue
        return(path)



graph().addNode("A")
graph().addNode("B")
graph().addNode("D")
graph().addNode("F")
graph().addNode("C")
graph().addNode("E")
graph().addNode("F")
graph().addNode("G")
graph().addNode("H")
graph().addNode("S")

graph().addEdge("A", "B")
graph().addEdge("A", "S")
graph().addEdge("S", "C")
graph().addEdge("S", "G")
graph().addEdge("C", "D")
graph().addEdge("C", "E")
graph().addEdge("C", "F")
graph().addEdge("E", "H")
graph().addEdge("F", "G")
graph().addEdge("G", "H")

print(graph().bfs("A"))
print(graph().dfs({},"A"))

f = open("print.txt", "w")
f.close()
f = open("print.txt", "a")
f.write("Breadth first search" + str(graph().bfs("A")))
f.write("Depth first search" + str(graph().dfs({},"A")))
f.close()




