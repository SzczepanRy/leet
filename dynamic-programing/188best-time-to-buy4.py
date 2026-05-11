class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """


        dp = [ [0 , -float("inf") ] for _ in range(k)]


        for price in prices:
            dp[0][1] = max(dp[0][1] , -price )
            dp[0][0] = max(dp[0][0] , dp[0][1] + price )
            for i in range(1,k):
                dp[i][1] = max(dp[i][1] , dp[i-1][0] -price )
                dp[i][0] = max(dp[i][0] , dp[i][1] + price )



        print(dp)


        return dp[-1][0]
        ## notholding ,  holding

k = 2
prices = [2,4,1]
prices = [3,2,6,5,0,3]
s = Solution()
s.maxProfit(k ,  prices)
