class Node:
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BinaryTree:
    
    def __init__(self):
        self.root=None
        
    def add(self,data):
        if not self.root:
            self.root=Node(data)
            return
        
        self.recursiveAdd(data,self.root)
        
    def recursiveAdd(self,data,node):
        if node.left is None:
            node.left=Node(data)
        elif node.right is None:
            node.right=Node(data)
        else:
            self.recursiveAdd(data,node.left)
    
    def display(self,depth=0,node=None):
        if node is None:
            node=self.root
            
        print(" " *depth,node.data)
        
        if node.left is not None:
            self.display(depth+1,node.left)
        
        if node.right is not None:
            self.display(depth+1,node.right)
        
            
BinaryTree=BinaryTree()
BinaryTree.add(5)
BinaryTree.add(1)
BinaryTree.add(2)
BinaryTree.add(3)
BinaryTree.add(4)
BinaryTree.add(5)
BinaryTree.display()
