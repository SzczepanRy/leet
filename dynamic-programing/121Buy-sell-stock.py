class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        minpri = float("inf")
        maxpro = 0

        for i in prices:

            if i < minpri:
                minpri = i

            elif i - minpri > maxpro:
                maxpro = i - minpri

        return maxpro

prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
s= Solution()
print(s.maxProfit(prices))
