class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1 :
            return 1
        if n ==2 :
            return 2
        if n ==0 :
            return 0

        dp = [0]*(n+1)

        dp[1]= 1
        dp[2]= 2

        j = 1
        while j < n-1 :
            dp[j+2] = dp[j]+ dp[j+1]
            j+=1



        print(dp[-1])
        return dp[-1]




s = Solution()
s.climbStairs(3)

