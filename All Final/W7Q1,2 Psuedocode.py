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
        while (length of stack) ≠ 0:
            stack.extend( nodes[stack[0]].adjacent)

            IF stack[0] not in path:
                path.append(stack.pop(0))
                
            ELSE IF stack[0] in path:
                stack.pop(0)
                
            IF length of (nodes.keys()) = (length of path):
                return(path)
                break the loop
            
    DFS(self, dic, nod, path <- []):
        for eachNode in  nodes.keys():
            dic[eachNode] <-  nodes[eachNode].adjacent
        stack <- [] 
        stack.append(nod)
        while stack ≠ None:
            x <- stack.pop()
            IF x not in path:
                path +<- [x]     
                stack +<- dic[x] 
        return(path)


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

return(graph().bfs("A"))
return(graph().dfs({},"A"))

f <- openfile("print.txt", "w")
f.closefile
f <- openfile("print.txt", "a")
f.writetofile("Breadth first search" + str(graph().bfs("A")))
f.writetofile("Depth first search" + str(graph().dfs({},"A")))
f.closefile

