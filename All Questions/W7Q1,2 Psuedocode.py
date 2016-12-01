CLASS Node():
    __INIT__(self, name):
         name <- name
         adjacent <- []

    ADDADJACENT(self, edge):
         adjacent.append(edge)

CLASS Graph():

    __INIT__(self, nodeDict <- {}):
        self.nodeDict <- nodeDict 
    
    ADDNODE(self, node):
         nodes[node.name] <- node

    ADDEDGE(self, edge1, edge2):
         nodes[edge1].addAdjacent(edge2)
         nodes[edge2].addAdjacent(edge1)
         #make connection 2 way between nodes

    BFS(self, nod):
        stack <- []
        stack.append(nod)
        path <- []
        while len(stack) ≠ 0:
            stack.extend( nodes[stack[0]].adjacent) #add contents of current node to stack

            IF stack[0] not in path:
                path.append(stack.pop(0))   #if node isnt in path list, pop and append to path
                
            ELSEIF stack[0] in path:        #if node is in path, pop node
                stack.pop(0)
                
            IF len( nodes.keys()) = len(path):      #check if all nodes are in path, return path and break loop
                RETURN(path)
                break the loop
            
    DFS(self, dic, nod, path=[]):
        for eachNode in  nodes.keys():
            dic[eachNode] <-  nodes[eachNode].adjacent #add first node to stack
        stack <- [] 
        stack.append(nod) #add first node to stack
        while stack ≠ None:
            x <- stack.pop()    #take of end node from stack
            IF x not in path:
                path += [x]     #add x to path
                stack += dic[x] #add dic[x] to stack
        RETURN(path)


graph().addNode(Node("A"))
graph().addNode(Node("B"))
graph().addNode(Node("D"))
graph().addNode(Node("F"))
graph().addNode(Node("C"))
graph().addNode(Node("E"))
graph().addNode(Node("F"))
graph().addNode(Node("G"))
graph().addNode(Node("H"))
graph().addNode(Node("S"))
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

RETURN(graph().bfs("A"))
RETURN(graph().dfs({},"A"))

f <- openfile("print.txt", "w")
f.closefile
f <- openfile("print.txt", "a")
f.writetofile("Breadth first search" + str(graph().bfs("A")))
f.writetofile("Depth first search" + str(graph().dfs({},"A")))
f.closefile

