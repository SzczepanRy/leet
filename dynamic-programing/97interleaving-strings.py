class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        # zadanie polega na szplicowaniu dwuch stringów tak aby slicy z karzdego były naprzemiennie

        n = len(s1)+1
        m = len(s2)+1

        if n+m-2 != len(s3):
            return False

        dp = [[False]*n for _ in range(m) ]


        dp[0][0]=True

        for i in range(1,n):
            if s1[i-1] == s3[i-1] and dp[0][i-1]:
                dp[0][i]= True


        for i in range(1,m):
            if s2[i-1] == s3[i-1] and dp[i-1][0]:
                dp[i][0]= True


        for i in range(1, m):
            for j in range(1, n):

                #bardz osmieszna zalerznoscc
                s3char = s3[i+j-1]

                topcheck = dp[i-1][j] and s3char == s2[i-1]

                leftcheck = dp[i][j-1] and s3char == s1[j-1]

                dp[i][j]= leftcheck or topcheck


        return dp[m-1][n-1]



s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

s = Solution()
s.isInterleave(s1,s2,s3)
