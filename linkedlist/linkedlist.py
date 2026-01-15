class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
def printlist(head):
    temp=head
        
    while temp is not None:
        print(temp.data,end="->")
        temp=temp.next
            
    print("Null")
    
def begin(head,data):
    new=Node(data)
    new.next=head
    head=new
    return head
    
def end(head,data):
    new=Node(data)
    if head is None:
        return new
        
    temp=head
    while temp.next is not None:
        temp=temp.next
    temp.next=new
    return head

def delete(head,key):
    if head is None:
        return head
    
    if head.data==key:
        return head.next
    temp=head
    
    while temp.next is not None:
        if temp.next.data==key:
            temp.next=temp.next.next
            break
        temp=temp.next
    return head
    
def rev(head):
    prev=None
    curr=head
    
    while curr is not None:
        next_node=curr.next
        
        curr.next=prev
        prev=curr
        curr=next_node
    return prev
        

node1=Node(10)
node2=Node(20)
node3=Node(30)

node1.next=node2
node2.next=node3
head=node1

head=rev(head)

printlist(head)