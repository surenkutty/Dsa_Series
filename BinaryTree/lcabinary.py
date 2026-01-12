class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root=None
    
    def insert(self,root,val):
        if root is None:
            return Node(val)
        if val < root.val:
            root.left = self.insert(root.left,val)
        else:
            root.right = self.insert(root.right,val)
        return root
    
    def lca(self,root,n1,n2):
        curr=root

        while curr:
            if n1<curr.val and n2<curr.val:
                curr=curr.left
            
            elif n1>curr.val and n2>curr.val:
                curr=curr.right
            else:
                return curr
        return None
    
    ''' Recursive approach'''

    def lca_recursive(self,root,n1,n2):
        if root is None:
            return None
        
        if n1<root.val and n2<root.val:
            return self.lca_recursive(root.left,n1,n2)
        
        if n1>root.val and n2>root.val:
            return self.lca_recursive(root.right,n1,n2)
        
        return root.val

tree = BinaryTree()
   
values = [20, 10, 30, 5, 15, 25, 35]
for val in values:
    tree.root = tree.insert(tree.root, val)
    
n1, n2 = 5, 15
lca_node = tree.lca(tree.root, n1, n2)
if lca_node:
    print(f"LCA of {n1} and {n2} is {lca_node.val}")
else:
    print("LCA not found")
