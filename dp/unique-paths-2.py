class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        cols = len(obstacleGrid[0])
        # dp[c] represents the number of ways to reach column 'c'
        dp = [0] * cols
        dp[0] = 1

        for row in obstacleGrid:
            for c in range(cols):
                if row[c] == 1:
                    # If there's an obstacle, 0 ways to reach this cell
                    dp[c] = 0
                elif c > 0:
                    # Ways to reach = paths from above (current dp[c])
                    # + paths from the left (dp[c-1])
                    dp[c] += dp[c-1]

        return dp[-1]


s = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(s.uniquePathsWithObstacles(obstacleGrid))

