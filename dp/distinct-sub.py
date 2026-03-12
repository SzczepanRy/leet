class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        n, m = len(s) , len(t)

        dp = [0*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1,n+1):
            for j in range(1,m+1):

                if s[i] == t[j]:
                    # Sumujemy: użycie litery + zignorowanie litery
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    # Litery inne: możemy tylko zignorować aktualną literę z 's'
                    dp[i][j] = dp[i-1][j]

        return dp[n][m]
