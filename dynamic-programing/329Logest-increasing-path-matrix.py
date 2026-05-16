class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """


        memo = {}

        n = len(matrix)
        m = len(matrix[0])

        def rekur(i , j ):

            if (i , j) in memo:
                return memo[(i,j)]

            max_len = 1
            for ri , rj in [(-1,0) , (0,-1) , (0,1) , (1,0)]:
                ni = i + ri
                nj = j + rj

                if ni >= 0 and ni < n and nj >= 0 and nj < m:
                    if matrix[i][j] < matrix[ni][nj]:
                        max_len= max( max_len , rekur(ni , nj) +1 )

            ## koniec naszej drogi
            memo[(i,j)] = max_len
            return max_len

        res = 1
        for i in range(n):
            for j in range(m):
                res = max( res , rekur(i, j ))
        return res







matrix = [[7,8,9],[9,7,6],[7,2,3]]
s = Solution()
print(s.longestIncreasingPath(matrix))
