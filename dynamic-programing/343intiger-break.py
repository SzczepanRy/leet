class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] *(n+1)

        for i in range(2 , n+1):
            for j in range(1 , i):

                # Sprawdzamy co jest lepsze dla reszty: sama liczba (i - j) czy jej rozbicie dp[i - j]
                reszta = max(i - j, dp[i - j])
                dp[i] = max(reszta * j , dp[i])


        return dp[-1]




s = Solution()
s.integerBreak(10)
