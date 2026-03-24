def amstrong(n):
    temp=n
    sum=0
    digits=len(str(n))
    while n>0:
        digit=n%10
        sum+=digit**digits
        n//=10
    if temp==sum:
        print(temp,"is an Amstrong number")
    else:        
        print(temp,"is not an Amstrong number")
amstrong(153)