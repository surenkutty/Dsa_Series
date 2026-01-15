class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def printlist(head):
    temp=head
        
    while temp is not None:
        print(temp.data,end=" <-> ")
        temp=temp.next
            
    print("Null")

def begin(head,data):
    new=Node(data)
    new.next=head
    if head is not None:
        head.prev=new
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
    new.prev=temp
    return head

def printreverse(head):
    temp=head
    if temp is None:
        return
    while temp.next is not None:
        temp=temp.next
    
    while temp is not None:
        print(temp.data,end=" <-> ")
        temp=temp.prev
    print("Null")


def begin(head,data):
    new=Node(data)
    new.next=head
    if head is not None:
        head.prev=new
    head=new
    return head

def end(head,data):
    new=Node(data)
    if head is None:
        return new
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=new
    new.prev=temp
    return head
def delete(head,key):
    if head is None:
        return head
    
    if head.data==key:
        head=head.next
        if head:
            head.prev=None
    temp=head
    while temp:
        if temp.data==key:
            if temp.next:
                temp.next.prev=temp.prev
            if temp.prev:
                temp.prev.next=temp.next
            break
        temp=temp.next
    return head


node1=Node(10)
node2=Node(20)
node3=Node(30)
node1.next=node2
node2.prev=node1
node2.next=node3
node3.prev=node2
head=node1
head=begin(head,5)
printlist(head)