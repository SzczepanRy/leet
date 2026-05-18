class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """


        memo = {}

        def rekur(i ,j ):

            if i >= j:
                return 0
            if (i , j ) in memo:
                return memo[(i,j)]

            minVal = float("inf")

            for k in range((i+j)//2 , j +1):
                # k jako root

                worstCase = k+max( rekur(i,k-1), rekur(k+1 , j))
                minVal = min(minVal , worstCase)


            memo[(i,j)] = minVal
            return minVal


        return rekur(1, n)









s = Solution()
s.getMoneyAmount(10)
