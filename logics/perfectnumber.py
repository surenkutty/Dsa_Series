def perfect(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    if sum==n:
        print(n,"is a perfect number")
    else:        
        print(n,"is not a perfect number")

perfect(28)