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
        self.nodeDict[edge1].addAdjacent(edge2)
        self.nodeDict[edge2].addAdjacent(edge1)


    def bfs(self, nod):
        stack = []
        stack.append(nod)
        path = []
        while len(stack) != 0:  
            stack.extend(self.nodeDict[stack[0]].adjacent)
            if stack[0] not in path:
                path.append(stack.pop(0))
            elif stack[0] in path:
                stack.pop(0)
            if len(self.nodeDict.keys()) == len(path):
                return(path)
                break


    def dfs(self, dic, nod, path=[]):
        for eachNode in self.nodeDict.keys():
            dic[eachNode] = self.nodeDict[eachNode].adjacent
        stack = []
        stack.append(nod)
        while (len(stack) != 0):
            x = stack.pop()
            if x not in path:   
                path += [x]
                stack += dic[x]
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




