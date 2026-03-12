#o(nxm)
#program tworzy tablie dwuwymiarową
# przykładowo biorąc wartość arr[i][j] , kad sprawdza wartość do góry  w lewo i skos góra lewo , jesli warość jsą takie mame to posataje kwadrat o rozmiarze arr[i][j] + 1

class Solution:
    def maximalSquare(self, matrix ):

        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    # Use (r+1, c+1) to handle boundaries easily without extra if-statements
                    dp[r+1][c+1] = min(dp[r][c+1], dp[r+1][c], dp[r][c]) + 1
                    max_side = max(max_side, dp[r+1][c+1])

        return max_side * max_side
