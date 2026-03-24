def fib(10):
    a=0
    b=1
    if n<=0:
        print("Invalid input")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            print(c)
            a=b
            b=c

fib(10)