class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if root is None:
            return Node(val)

        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root
    
    def inorder(root):
        stack=[]
        curr=root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left
            
            curr=stack.pop()
            print(curr.val,end=" ")
            curr=curr.right

    def preorder(root):
        if root is None:
            return
        stack=[root]

        while stack:
            node=stack.pop()
            print(node.val,end=" ")

            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

    def postorder(root):
        if root is None:
            return
        
        s1=[root]
        s2=[]

        while s1:
            node=s1.pop()
            s2.append(node)

            if root.left:
                s1.append(root.left)
            if root.right:
                s1.append(root.right)
        while s2:
            print(s2.pop().val,end=" ")
    
