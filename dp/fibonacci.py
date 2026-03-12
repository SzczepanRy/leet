class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 :
            return 1

        dp = [0]*(n+1)
        dp[1]=1

        t= 0
        while t < n-1:
            dp[t+2] = dp[t] + dp[t+1]
            t+=1

        print(dp[-1])
        return dp[-1]




s= Solution()
s.fib(3)
