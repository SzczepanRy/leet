class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """


        n = len(prices)
        dp = [[0]*2  for _ in range(n)]

        # [][0] - brak akcji , [][1] - posidanie akcji

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1,n):
            # albo nic nie robimy , albo sprzedajeny akcje
            dp[i][0] = max(dp[i-1][0] , dp[i-1][1] + prices[i])
            # albo nic nie robimy mamy acje  , albo kupujemy akcje
            dp[i][1] = max(dp[i-1][1] , dp[i-1][0] - prices[i])

        return dp[n-1][0]


prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(prices))
