class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for _ in range(n+1)]
        dp[0]=[""]

        for j in range(1 , n+1):
            for i in range(j):
                # Formuła: "(" + dp[i] + ")" + dp[j - 1 - i]
                for left in dp[i]:
                    for right in dp[j-i-1]:
                        dp[j].append("("+left+")" + right)

        return dp[n]

s = Solution()
s.generateParenthesis(3)
