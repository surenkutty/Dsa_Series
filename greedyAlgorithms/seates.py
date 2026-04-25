def min_moves(seat):
    pos=[]
    
    for i in range(len(seat)):
        if seat[i]=='x':
            pos.append(i)
            
    adjusted=[]
    for i in range(len(pos)):
        adjusted.append(pos[i]-i)
        
    mid=len(adjusted)//2
    median=adjusted[mid]
    mov=0
    
    for val in adjusted:
        mov+=abs(val-median)
        
    return mov
    
if __name__=="__main__":
    
    seat=list(map(str,input("enter the seats: ").split()))
    
    print(min_moves(seat))