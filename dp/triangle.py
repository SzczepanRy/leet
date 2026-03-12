class Solution:
    def minimumTotal(self, triangle):
        oldp=triangle[0]

        for i in range(1,len(triangle)):
            n = len(triangle[i])
            dp=["."]*n
            for j in range(len(oldp)):
                ## dla j i j+1 dodajecierzki

                if dp[j]==".":
                    dp[j]= oldp[j] + triangle[i][j]
                    if j +1 < n:
                        dp[j+1]= oldp[j] + triangle[i][j+1]
                else:
                    dp[j]=min(dp[j], oldp[j] + triangle[i][j])
                    if j +1 < n:
                        if dp[j+1] != ".":
                            dp[j+1]=min(dp[j+1], oldp[j] + triangle[i][j+1])
                        else:
                            dp[j+1]= oldp[j] + triangle[i][j+1]

            oldp=dp

        return min(oldp)

triangle =[[-1],[2,3],[1,-1,-1]]
s=Solution()
print(s.minimumTotal(triangle))



