class Solution:
    def minFallingPathSum(self, matrix):

        oldp = matrix[0]
        inf = float("inf")

        for i in range(1, len(matrix)):
            n = len(matrix[i])
            dp=[inf]*(n)
            for j in range(n):

                dp[j]=min(matrix[i][j] + oldp[j] ,dp[j] )
                if j-1 >=0 :
                    dp[j-1]=min(matrix[i][j-1] + oldp[j] ,dp[j-1] )

                if j+1<n :
                    dp[j+1]=min(matrix[i][j+1] + oldp[j] ,dp[j+1] )

            print(dp)
            oldp=dp

        return min(oldp)


matrix = [[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]
s = Solution()
print(s.minFallingPathSum(matrix))
