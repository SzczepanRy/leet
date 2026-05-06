class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n=numRows+1
        if n == 0:
            return [[1]]


        dp = [[1]*i for i in range(1,n+1) ]

        for i in range(2 , len(dp)):
            lastArr= dp[i-1]

            for j in range(1,len(lastArr)):
                el1 = lastArr[j-1]
                el2 = lastArr[j]
                dp[i][j] = el1+el2


        return dp[-1]

s= Solution()
print(s.generate(1))
