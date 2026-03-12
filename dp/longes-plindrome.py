#generuje dwu wymiarową tablice, dp ,
#skos wypełniam true , bo pojedyńcze litery są polindormiczne
#sprawdzam zkkresy wieksze lub równe dwa od i do j jeśli wartość na połorzniu
# i+1 j-1 jest prawdziwa to znaczy że wartość od i-1 do j-1 jest palindormem ,
# jeśli s[i]==s[j] i wcześniejsze załorznia spełnione to osnaczam pozycje dp[i][j] jako prawde
# by mogła być wykorzystana w  nastempnej teracji
class Solution:
    def longestPalindrome(self, s):
        if len(s) <2:
            return s
        n=len(s)

        res = s[0]
        dp = [[False] * n for _ in range(n) ]

        for i in range(n):
            dp[i][i]=True

        for length in range(2,n+1):

            for i in range(n- length +1):
                j = i +length-1

                if s[i] == s[j]:
                    if length ==2 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if len(s[i:j+1])> len(res):
                            res = s[i:j+1]






        print("result " ,res)
        return res


s = Solution()
s.longestPalindrome("jdjjdjddhf")



