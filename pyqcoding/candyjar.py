class CandyJar:
    def __init__(self):
        self.capacity=10
        self.min_candies=5
        self.current=10
        
        
    def order(self,qty):
        if qty<=self.current-self.min_candies:
            self.current=self.current-qty
            print("Order accepeted")
        else:
            print("Order denied -Minimum level reached")
            
    def refill(self):
        if self.current<self.min_candies:
            print("Refilling jat...")
            self.current=self.capacity
            
    def display(self):
        print("candies left:",self.current)
        
jar=CandyJar()

while True:
    print("\n1. Order \n2.refill \n3.Display \n4.Exit")
    choice=int(input("Enter choice:"))
    
    if choice==1:
        qty=int(input("Enter number of candies:"))
        jar.order(qty)
    elif choice==2:
        jar.refill()
    elif choice==3:
        jar.display()
        
    else:
        break