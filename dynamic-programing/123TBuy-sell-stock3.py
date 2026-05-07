class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        ## only 2 transactions

        sell1 = sell2 = 0
        buy1 = buy2 = -float("inf")

        for price in prices:

            # kupno piwerwzej akacji
            buy1 = max( buy1 , -price)

            # sprzedar pierwszej akcji
            sell1 = max(sell1 , buy1 + price )

            #
            buy2 = max(buy2 , sell1 - price)

            sell2 = max(sell2 , buy2 + price )

        return sell2





prices = [3,3,5,0,0,3,1,4]

s= Solution()
s.maxProfit(prices )
