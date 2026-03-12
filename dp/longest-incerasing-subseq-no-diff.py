class Solution(object):
    def longestArithSeqLength(self, nums):

        n = len(nums)
        dp =[{} for _ in range(n)]

        max_len= 2
        for i in range(1,n):
            for j in range(i):
                r = nums[i] -nums[j]

                if r in dp[j]:
                    dp[i][r] = dp[j][r]+ 1
                else:
                    dp[i][r]=2

                if dp[i][r] > max_len:
                    max_len = dp[i][r]

        return max_len



nums = [20,1,15,3,10,5,8]
s = Solution()
s.longestArithSeqLength(nums)



