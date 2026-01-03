
def climb(cost):
    n=len(cost)
    dp=[0]*n
    dp[0]=cost[0]
    dp[1]=cost[1]
    for i in range(2,n):
        dp[i]=cost[i]+min(dp[i-1],dp[i-2])
    return min(dp[n-1],dp[n-2])

cost=[10,15,20]
print(climb(cost))

'''
or
'''
def climb(cost):
    for i in range(2,len(cost)):
        cost[i]+=min(cost[i-1],cost[i-2])
    return min(cost[-1],cost[-2])