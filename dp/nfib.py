class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0]*(n+1)

        if n ==1 :
            return 1
        if n == 2:
            return 2

        dp[1]=1
        dp[2]=1
        dp[3] =2
        t=1
        while t< n-2:
            dp[t+3] = dp[t]+dp[t+2]+dp[t+1]
            t+=1

        return dp
















s = Solution()

s.tribonacci(4)

