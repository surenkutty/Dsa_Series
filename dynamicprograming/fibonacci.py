def fib(n):
    dp=[0] * (n)
    dp[0]=0
    if n>1:
        dp[1]=1 
    for i in range(2,n):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n-1]

'''
This is bottom-up dynamic programming approach to calculate the nth Fibonacci number.
or
'''
def fib(n):
    if n<=2:
        return 1
    dp=[0] * (n)
    dp[0],dp[1]=1,1
    for i in range(2,n):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[-1]


""" 
THis is Top to bottom approach to calculate the nth Fibonacci number.
"""

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    memo[n]=fib(n-1,memo)+fib(n-2,memo)
    return memo[n]
print(fib(6))  # Output: 8