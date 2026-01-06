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

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)
            
    def preorder(self,root):
        if root:
            print(root.val,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val,end=" ")

    def search(self, root, key):
        if root is None:
            return False

        if root.val == key:
            return True
        elif key < root.val:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)
    def height(self,root):
        if root is None:
            return 0
        return 1+max(self.height(root.left),self.height(root.left))
    def deleteNode(self,root,key) :
        if not root:
            return root

        if key>root.val:
            root.right=self.deleteNode(root.right,key)
        elif key<root.val:
            root.left=self.deleteNode(root.left,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            curr=root.right
            while curr.left:
                curr=curr.left
            root.val=curr.val
            root.right=self.deleteNode(root.right,root.val)
        return root

t=Tree()
values = [10, 5, 15, 3, 7, 12]


for v in values:
    t.root = t.insert(t.root, v)

print("Inorder traversal:")
t.inorder(t.root)
print("\npreorder traversal:")
t.preorder(t.root)
print("\npostorder traversal:")
t.postorder(t.root)


print("\nHeight of tree:", t.height(t.root))
