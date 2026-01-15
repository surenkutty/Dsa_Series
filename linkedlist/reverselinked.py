class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def rev(head):
    prev=None
    curr=head
     
    while curr is not None:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node
    return prev

def printlist(head):
    temp=head
        
    while temp is not None:
        print(temp.data,end="->")
        temp=temp.next
            
    print("Null")

node1=Node(10)
node2=Node(20)
node3=Node(30)


node1.next=node2
node2.next=node3
head=node1

rev_head=rev(head)
printlist(rev_head)