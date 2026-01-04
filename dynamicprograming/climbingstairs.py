def climb(n):
    if n<=2:
        return n
    dp=[0] * (n+1)
    dp[0]=1
    dp[1]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

print(climb(4))  # Output: 5

