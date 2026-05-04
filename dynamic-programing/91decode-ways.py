class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s[0] == "0":
            return 0

        n = len(s)
        dp = [0]*(n+1)
        dp[0]=1
        dp[1]=1


        for i in range(2,n+1):
            s1 = s[i-1]
            if s1 != "0":
                dp[i] +=  dp[i-1]


            s2 = s[i-2]
            num = int(s2+s1)
            if 10<=num <=26:
                dp[i]+=dp[i-2]


        return dp[-1]





s = Solution()
s.numDecodings("226")
