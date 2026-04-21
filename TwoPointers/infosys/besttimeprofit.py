def sellmaxprofit(prices):
    minprice=float('inf')
    max_profit=0
    
    for i in prices:
        if i<minprice:
            minprice=i
        else:
            profit=i-minprice
            max_profit=max(max_profit,profit)
    return max_profit
        
if __name__=="__main__":
    arr=list(map(int,input("enter input:").split()))
    print(sellmaxprofit(arr))