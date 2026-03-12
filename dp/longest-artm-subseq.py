class Solution:
    def longestArithSeqLength(self, nums) :

        nums = sorted(nums)
        n = len(nums)
        dp = [1]*n

        print(dp)

        for i in range(1,n):
            for j in range(i):

                r = nums[i] - nums[j]
                if r < n and r >=0:
                    print(r)
                    dp[r]+=1

        print(dp)
        return max(dp)

nums = [20,1,15,3,10,5,8]
s = Solution()
s.longestArithSeqLength(nums)
