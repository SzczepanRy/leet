class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n= len(s)
        dp=[[Fasle]*(n) for _ in range(n) ]

        for i in range(n+1):
            dp[i][i]=True

        for length in range(n):
            for i in range(n- length +1):
                j = i +length-1

                if s[i] == s[j]:
                    if length == 2 or dp[i+1][j-1] :
                        dp[i][j]=True



