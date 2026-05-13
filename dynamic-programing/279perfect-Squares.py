class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [float("inf")]*(n+1)

        dp[0]=0

        for i in range(1,n+1):

            j = 1
            while j**2 <=i:

                dp[i] = min(dp[i] , dp[i-j**2] +1)

                j+=1

        return dp[-1]







s=Solution()
s.numSquares(13)
