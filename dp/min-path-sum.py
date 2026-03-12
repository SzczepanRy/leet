class Solution:
    def minPathSum(self, grid) :
        # down or right
        #mxn
        n= len(grid)
        m = len(grid[0])

        dp = [0]*m
        dp[0] = grid[0][0]

        ## init lewej srtony

        for r in range(1,m):
            if dp[r-1] != -1:
                dp[r] = dp[r-1] + grid[0][r]

        for c in range(1,n):
            dp[0] += grid[c][0]

            for r in range(1,m):
                dp[r] = grid[c][r]+ min(dp[r] , dp[r-1])

        return dp[-1]



grid = [[1,3,1],[1,5,1],[4,2,1]]
s = Solution()
print(s.minPathSum(grid))

