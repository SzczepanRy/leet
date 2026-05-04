class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        dp= [[int(i) for i in arr] for arr in matrix ]
        print(dp)

        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):

                if dp[i][j] != 0:
                    dp[i][j] += dp[i-1][j]

        max_area=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                h = dp[i][j]

                width = 1

                l = j-1
                while l >-1 and dp[i][l]>=h:
                    width +=1
                    l-=1

                r = j+1
                while r < len(matrix[0]) and dp[i][r]>=h:
                    width +=1
                    r+=1


                max_area = max( max_area , width*h)

        return max_area




matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["0"]]
s = Solution()
print(s.maximalRectangle(matrix))
