#include <iostream>

class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

        
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree


def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)
  

def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print(tree.value)
    if(tree.right!=None):
        in_order(tree.right)
        

def iterative_in_order(tree):
    stack = []
    while True:
        if tree != None:
            stack.append(tree)      #append location on left to top of stack
            tree = tree.left        #set tree to left node
        else:                       #if tree == none
            if(len(stack) > 0):     #check stack length
               tree = stack.pop()   #remove item from stack top, then set == tree
               print(tree.value)    #print value
               tree = tree.right
               continue             #go to right node and continue
            else:
                break
            
    
    

if __name__ == '__main__':
    
    t=tree_insert(None,6);
    tree_insert(t,10)
    tree_insert(t,5)
    tree_insert(t,2)
    tree_insert(t,3)
    tree_insert(t,4)
    tree_insert(t,11)
    #in_order(t)
    iterative_in_order(t)


