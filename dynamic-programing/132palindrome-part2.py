class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(s)

        n = len(s)


        #czy s[i:j] jest pal >
        dp = [[0]*n for _ in range(n)]

        for i in range(n):
            dp[i][i]=1
            if i+1 < n and s[i] == s[i+1]:
                dp[i][i+1]=1


        for arr in dp:
            print(arr)
        print("NNNNNNNNNNNNNNNNNNNNNNNN")


        for L in range(1, n+1):
            for i in range(n -L+1 ):
                j = i+L-1

                if s[i] == s[j]:
                    if i +1 < n and j-1 >=0  :
                        if dp[i+1][j-1] == 1 or L <3 :
                            dp[i][j]=1


        for arr in dp:
            print(arr)





        cuts = [0] * n
        for i in range(n):
            res = i

            for j in range(i + 1):
                # Jeśli s[j...i] jest palindromem
                if dp[j][i]:
                    # Jeśli zaczyna się od początku stringa, 0 cięć
                    if j == 0:
                        res = 0
                    else:
                        # W przeciwnym razie: cięcia dla s[0...j-1] + 1 cięcie
                        res = min(res, cuts[j-1] + 1)

            cuts[i] = res

        return cuts[n-1]










s = Solution()
print(s.minCut("adavfdad"))
